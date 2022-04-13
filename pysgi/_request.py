# this file has all the code that handles
# requests coming from a client.

from http_parser.pyparser import HttpParser


def parser_http(http_message: str) -> dict:
    parser = HttpParser()
    parser.execute(http_message, len(http_message))

    http_content = {}

    http_content['path'] = parser.get_path()
    http_content['query'] = parser.get_query_string()
    http_content['method'] = parser.get_method()

    if parser.is_headers_complete():
        http_content['headers'] = parser.get_headers()

    if parser.is_partial_body():
        http_content['body'] = parser.recv_body()

    return http_content
