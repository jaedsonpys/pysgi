CONTENT_TYPE = 'text/html'
SERVER_NAME = 'PySGI'


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

    http_message = '\n\r\r'.join(http)
    return http_message
