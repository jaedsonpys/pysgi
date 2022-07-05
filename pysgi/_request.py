# this file has all the code that handles
# requests coming from a client.

from typing import Union
from socket import timeout as sock_timeout
from threading import Thread
from types import FunctionType
from typing import Any
from urllib.parse import unquote

from http_parser.pyparser import HttpParser

from ._sockethandler import Client
from .response import Response, make_response
from .route import Route
from ._print import print_response


class Request(object):
    def __init__(self, routes: dict[Route]) -> None:
        self._routes = routes

    def handle_request(self, client: Client) -> None:
        # create a thread to handle request
        ct = Thread(target=self._handle_request, args=(client,))
        ct.start()

    def get_route(self, path: str) -> Union[Route, dict]:
        path_split = path.split('/')
        result = {}
        
        while '' in path_split:
            path_split.remove('')

        for r in self._routes.values():
            route_find = False

            if r.path == path:
                return r, result
            elif len(path_split) == (len(r.parameters) + len(r.no_parameters)):
                # checking if routes that are not parameters are available
                for a in r.no_parameters:
                    if path_split[a['index']] == a['name']:
                        route_find = True
                    else:
                        route_find = False
                        break

                # if the route was found get its arguments
                if route_find:
                    for d in r.parameters:
                        index = d['index']
                        var_type = d['var_type']
                        name = d['name']

                        variable = path_split[index]
                        
                        if var_type == 'str':
                            variable = str(variable)
                        elif var_type == 'int':
                            variable = int(variable)
                        elif var_type == 'float':
                            variable = float(variable)

                        result[name] = variable

                    return r, result

        # if the code got here it means no
        # dynamic route or default route found
        return None, {}

    def _handle_request(self, client: Client) -> None:
        client.csocket.settimeout(2.5)

        try:
            client_msg = client.csocket.recv(1024)
        except sock_timeout:
            # in this situation, the client has not
            # sent any message to the server, and
            # therefore its request cannot be processed,
            # closing the connection with the client
            # without returning anything.
            
            client.csocket.close()
            return None
        else:
            client.csocket.settimeout(None)
            
        request = ClientRequest()
        request.parser_http(client_msg)

        if request.is_valid() is False:
            # returning status 400 for invalid requests
            response = Response('Bad Request', 400)
            return self._send_response(client, response)

        request.host = client.host
        route_info, parameters = self.get_route(request.path)
        request.parameters = parameters

        # if the route is not found
        if not route_info:
            response = Response('Not Found', status=404)
        else:
            if request.method not in route_info.allowed_methods:
                response = Response('Method Not Allowed', status=405)
            else:
                route_function: FunctionType = route_info.function

                try:
                    function_response = route_function.__call__(request)
                except TypeError:
                    function_response = route_function.__call__()

                if isinstance(function_response, tuple):
                    # getting body and status of response 
                    # in use cases of: return "Hello", 200.
                    body, status = function_response
                    response = Response(body, status=status)
                elif isinstance(function_response, str):
                    response = Response(function_response)
                elif isinstance(function_response, Response):
                    response = function_response

        self._send_response(client, response)

        path = f'{request.path}{"?" if request.query_string else ""}{request.query_string}'
        print_response(response.status, path, request.method, client.host)

    @staticmethod
    def _send_response(client: Client, response: Response) -> None:
        http_response = make_response(response)
        client.csocket.send(http_response.encode())
        client.csocket.close()


class ClientRequest(object):
    def __init__(self) -> None:
        self.body: Any = None
        self.method: str = None
        self.path: str = None
        self.headers: dict = {}
        self.args: dict = {}
        self.parameters: dict = {}
        self.host: str = None

    def is_valid(self) -> bool:
        return self.path is not None    

    def _parse_args(self, query_string: str):
        args_list = query_string.split('&')
        args = {}

        for a in args_list:
            name, value = a.split('=')
            args[name] = value

        return args

    def parser_http(self, http_message: str) -> None:
        parser = HttpParser()
        parser.execute(http_message, len(http_message))

        path = parser.get_path()

        self.path = path if not path else unquote(path)
        self.method = parser.get_method()

        self.query_string = parser.get_query_string()

        if self.query_string:
            args = self._parse_args(self.query_string)
            self.args = args

        if parser.is_headers_complete():
            self.headers = parser.get_headers()

        if parser.is_partial_body():
            self.body = parser.recv_body()

    def __repr__(self) -> str:
        return (f'ClientRequest(path={self.path}, method={self.method},'
                f'headers={self.headers}, args={self.args}, body={self.body}, host={self.host})')
