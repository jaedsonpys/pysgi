CONTENT_TYPE = 'text/html'
SERVER_NAME = 'PySGI'


class Response(object):
    body: str
    status: int
    headers: dict
    cookies: dict
    _full_message: str

    def set_header(self, key: str, value: str) -> None:
        self.headers[key] = value

    def set_cookie(self, key: str, value: str) -> None:
        self.cookies[key] = value
    
    def set_status(self, status: int) -> None:
        if isinstance(status, int):
            self.status = status
        else:
            raise TypeError(f'The "status" argument must be of type integer, not {type(status)}')


def make_response(
    body: str,
    status: int = 200,
    headers: dict = None,
    cookies: dict = None
) -> str:
    http = list()
    http.append(f'HTTP/1.1 {status}')

    used_headers = list()

    # set default headers
    http.append(f'Server: {SERVER_NAME}')

    if headers:
        for key, value in headers.items():
            if key not in used_headers:
                header_str = f'{key}: {value}'
                used_headers.append(key)
                http.append(header_str)
    else:
        http.append(f'Content-Type: {CONTENT_TYPE}')

    if cookies:
        cookies_list = []

        for key, value in cookies.items():
            cookie_str = f'{key}={value}'
            cookies_list.append(cookie_str)

        cookie_header = 'Set-Cookie: ' + '; '.join(cookies_list)
        http.append(cookie_header)

    # defining the body of the response
    http.append('')
    http.append(body)

    http_message = '\n'.join(http)
    return http_message
