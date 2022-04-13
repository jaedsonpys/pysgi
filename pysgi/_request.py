# this file has all the code that handles
# requests coming from a client.

from types import FunctionType
from typing import Any
from http_parser.pyparser import HttpParser

from ._sockethandler import Client
from .route import Route
from .response import make_response

from threading import Thread


class Request(object):
    def __init__(self, routes: dict[Route]) -> None:
        self._routes = routes

    def handle_request(self, client: Client) -> None:
        # create a thread to handle request
        ct = Thread(target=self._handle_request, args=(client,))
        ct.start()

    def _handle_request(self, client: Client) -> None:
        parse = parser_http(client.message)

        if parse.is_valid() is False:
            # returning status 400 for invalid requests
            response = make_response('Bad Request', 400)
            return self._send_response(client, response)

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
                    route_view = route_function.__call__(route_info)
                except TypeError:
                    route_view = route_function.__call__()

                response = route_view
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
        return self.path and self.method

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
