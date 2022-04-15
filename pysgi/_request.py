# this file has all the code that handles
# requests coming from a client.

from socket import timeout as sock_timeout
from threading import Thread
from types import FunctionType
from typing import Any

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
            response = make_response('Bad Request', 400)
            return self._send_response(client, response)

        route_info = self._routes.get(request.path)

        # if the route is not found
        if route_info is None:
            response = make_response('Not Found', status=404)
        else:
            request_method = request.method

            # if the request method is accepted, the
            # request is handled
            if request_method in route_info.allowed_methods:
                route_function: FunctionType = route_info.function

                try:
                    function_response = route_function.__call__()
                except TypeError:
                    function_response = route_function.__call__(request)

                if isinstance(function_response, tuple):
                    # getting body and status of response 
                    # in use cases of: return "Hello", 200.
                    body, status = function_response
                    response = make_response(body, status=status)
                elif isinstance(function_response, str):
                    response = make_response(function_response)
                elif isinstance(function_response, Response):
                    response = function_response
            else:
                response = make_response('Method Not Allowed', status=405)

        self._send_response(client, response)
        print_response(response.status, request.path, request.method, client.host)

    @staticmethod
    def _send_response(client: Client, response: Response) -> None:
        client.csocket.send(response.get_http_message().encode())
        client.csocket.close()


class ClientRequest(object):
    body: Any
    method: str
    path: str
    headers: dict
    args: dict

    def is_valid(self) -> bool:
        return self.path is not None    

    def parser_http(self, http_message: str) -> None:
        parser = HttpParser()
        parser.execute(http_message, len(http_message))

        self.path = parser.get_path()
        self.args = parser.get_query_string()
        self.method = parser.get_method()

        if parser.is_headers_complete():
            self.headers = parser.get_headers()

        if parser.is_partial_body():
            self.body = parser.recv_body()

    def __repr__(self) -> str:
        return f'ClientRequest(path={self.path}, method={self.method},' \
               f'headers={self.headers}, args={self.args}, body={self.body})'
