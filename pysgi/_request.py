# this file has all the code that handles
# requests coming from a client.

from socket import timeout as sock_timeout
from threading import Thread
from types import FunctionType
from typing import Any

from http_parser.pyparser import HttpParser

from ._sockethandler import Client
from .response import make_response
from .route import Route
from ._print import print_request


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

        parse = parser_http(client_msg)

        if parse.is_valid() is False:
            # returning status 400 for invalid requests
            response = make_response('Bad Request', 400)
            return self._send_response(client, response)

        print_request(parse.path, parse.method, client.host)
        route_info = self._routes.get(parse.path)

        # if the route is not found
        if route_info is None:
            response = make_response('Not Found', status=404)
        else:
            request_method = parse.method

            # if the request method is accepted, the
            # request is handled
            if request_method in route_info.allowed_methods:
                route_function: FunctionType = route_info.function

                try:
                    response = route_function.__call__()
                except TypeError:
                    response = route_function.__call__(parse)

                if isinstance(response, str) is False:
                    raise ValueError(f'The function of a route must return a string, not "{type(response)}"')
            else:
                response = make_response('Method Not Allowed', status=405)

        self._send_response(client, response)

    @staticmethod
    def _send_response(client: Client, response: str) -> None:
        client.csocket.send(response.encode())
        client.csocket.close()


class ClientRequest(object):
    body: Any
    method: str
    path: str
    headers: dict
    args: dict

    def is_valid(self) -> bool:
        return self.path is not None

    def __repr__(self) -> str:
        return f'ClientRequest(path={self.path}, method={self.method},' \
               f'headers={self.headers}, args={self.args}, body={self.body})'


def parser_http(http_message: str) -> ClientRequest:
    parser = HttpParser()
    parser.execute(http_message, len(http_message))

    client_request = ClientRequest()

    client_request.path = parser.get_path()
    client_request.args = parser.get_query_string()
    client_request.method = parser.get_method()

    if parser.is_headers_complete():
        client_request.headers = parser.get_headers()

    if parser.is_partial_body():
        client_request.body = parser.recv_body()

    return client_request
