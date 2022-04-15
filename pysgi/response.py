from typing import Union
import json


SERVER_NAME = 'PySGI'


class Response(object):
    body: str
    status: int
    headers: dict = {}
    cookies: dict = {}
    _http_message: str

    def set_header(self, key: str, value: str) -> None:
        self.headers[key] = value

    def set_cookie(self, key: str, value: str) -> None:
        self.cookies[key] = value
    
    def set_status(self, status: int) -> None:
        if isinstance(status, int):
            self.status = status
        else:
            raise TypeError(f'The "status" argument must be of type integer, not {type(status)}')

    def set_body(self, body: str) -> None:
        self.body = body

    def set_http_message(self, http_message: str) -> None:
        self._http_message = http_message

    def get_http_message(self) -> str:
        return self._http_message


def make_response(
    body: Union[str, dict, list],
    status: int = 200,
    content_type: str = 'text/html',
    headers: dict = None,
    cookies: dict = None
) -> Response:
    http = list()
    http.append(f'HTTP/1.1 {status}')

    used_headers = list()

    # set default headers
    http.append(f'Server: {SERVER_NAME}')
    http.append(f'Content-Type: {content_type}')

    response = Response()
    response.set_status(status)
    response.set_header('Content-Type', content_type)
    response.set_header('Server', SERVER_NAME)

    if headers:
        for key, value in headers.items():
            if key not in used_headers:
                header_str = f'{key}: {value}'
                used_headers.append(key)
                http.append(header_str)
                response.set_header(key, value)

    if cookies:
        cookies_list = []

        for key, value in cookies.items():
            cookie_str = f'{key}={value}'
            cookies_list.append(cookie_str)
            response.set_cookie(key, value)

        cookie_header = 'Set-Cookie: ' + '; '.join(cookies_list)
        http.append(cookie_header)

    # defining the body of the response
    http.append('')
    
    # if the body is a JSON
    if isinstance(body, dict) or isinstance(body, list):
        body_data = json.dumps(body)
    elif isinstance(body, str):
        body_data = body
    else:
        # body type not accepted
        raise TypeError(f'The body argument can be "dict", "list", and "str", but not {type(body)}')

    http.append(body_data)
    response.set_body(body_data)

    http_message = '\n'.join(http)
    response.set_http_message(http_message)

    return response
