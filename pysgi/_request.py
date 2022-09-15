# this file has all the code that handles
# requests coming from a client.

from socket import timeout as sock_timeout
from threading import Thread
from types import FunctionType
from typing import Union

import http_pyparser

from ._sockethandler import Client
from .response import Response, make_response
from .route import Route
from .utils._print import print_response
from .utils.default_responses import DefaultResponses


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
            
        parser = http_pyparser.HTTPParser()

        try:
            request = parser.parser(client_msg.decode())
        except http_pyparser.exceptions.InvalidHTTPMessageError:
            return self._send_response(client, DefaultResponses.bad_request)

        route_info, parameters = self.get_route(request.path)
        request.parameters = parameters

        # if the route is not found
        if not route_info:
            response = DefaultResponses.not_found
        else:
            if request.method not in route_info.allowed_methods:
                response = DefaultResponses.method_not_allowed
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
        print_response(response.status, request.real_path, request.method, client.host)

    @staticmethod
    def _send_response(client: Client, response: Response) -> None:
        http_response = make_response(response)
        client.csocket.send(http_response.encode())
        client.csocket.close()
