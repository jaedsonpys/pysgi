# this file has all the code that handles
# requests coming from a client.

from typing import Any
from http_parser.pyparser import HttpParser


class ClientRequest(object):
    body: Any
    method: str
    path: str
    headers: dict
    args: dict

    def __repr__(self) -> str:
        return f'ClientRequest(path={self.path}, method={self.method}, \
                headers={self.headers}, args={self.args}, body={self.body})'


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
