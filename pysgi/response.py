CONTENT_TYPE = 'text/html'
SERVER_NAME = 'PySGI'


class Response(object):
    body: str
    status: int
    headers: dict
    cookies: dict
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
    body: str,
    status: int = 200,
    headers: dict = None,
    cookies: dict = None
) -> Response:
    http = list()
    http.append(f'HTTP/1.1 {status}')

    used_headers = list()

    # set default headers
    http.append(f'Server: {SERVER_NAME}')

    response = Response()
    response.set_status(status)
    response.set_header('Server', SERVER_NAME)

    if headers:
        for key, value in headers.items():
            if key not in used_headers:
                header_str = f'{key}: {value}'
                used_headers.append(key)
                http.append(header_str)
                response.set_header(key, value)
    else:
        http.append(f'Content-Type: {CONTENT_TYPE}')
        response.set_header('Content-Type', CONTENT_TYPE)

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
    http.append(body)
    response.set_body(body)

    http_message = '\n'.join(http)
    response.set_http_message(http_message)

    return response
