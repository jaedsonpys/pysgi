from typing import Union
import json

SERVER_NAME = 'PySGI'


class Response(object):
    """This class stores information from your response.
    Use to create more complex responses"""

    def __init__(
        self,
        body: Union[str, dict, list],
        status: int = 200,
        content_type: str = 'text/html',
    ) -> None:
        """Create a response.

        :param body: Body.
        :type body: Union[str, dict, list]
        :param status: HTTP status code, defaults to 200
        :type status: int, optional
        :param content_type: Response content type, defaults to 'text/html'
        :type content_type: str, optional
        """

        self.body: Union[str, dict, list] = body
        self.status: int = status
        self.content_type: str = content_type

        self.cookies: dict = {}
        self.headers: dict = {}

    def set_cookie(self, name: str, value: str) -> None:
        """Set a cookie"""
        self.cookies[name] = value

    def set_header(self, name: str, value: str) -> None:
        """Set a header"""
        self.headers[name] = value

    def __repr__(self) -> str:
        return f'Response(body={self.body}, status={self.status}, content_type={self.content_type}, '\
               f'cookies={self.cookies}, headers={self.headers})'


def make_response(response_obj: Response) -> str:
    """Create an HTTP message from the
    Response object.

    :param response_obj: Response object.
    :type response_obj: Response
    :raises TypeError: If the body's data type is not "str", "dict" or "list".
    :return: Returns the HTTP message
    :rtype: str
    """

    http = list()
    http.append(f'HTTP/1.1 {response_obj.status}')

    used_headers = list()

    # set default headers
    http.append(f'Server: {SERVER_NAME}')
    http.append(f'Content-Type: {response_obj.content_type}')

    if response_obj.headers:
        for key, value in response_obj.headers.items():
            if key not in used_headers:
                header_str = f'{key}: {value}'
                used_headers.append(key)
                http.append(header_str)

    if response_obj.cookies:
        cookies_list = []

        for key, value in response_obj.cookies.items():
            cookie_str = f'{key}={value}'
            cookies_list.append(cookie_str)

        cookie_header = 'Set-Cookie: ' + '; '.join(cookies_list)
        http.append(cookie_header)

    # defining the body of the response
    http.append('')
    
    # if the body is a JSON
    if isinstance(response_obj.body, dict) or isinstance(response_obj.body, list):
        body_data = json.dumps(response_obj.body)
    elif isinstance(response_obj.body, str):
        body_data = response_obj.body
    else:
        # body type not accepted
        raise TypeError(f'The body argument can be "dict", "list", and "str", but not {type(response_obj.body)}')

    http.append(body_data)

    http_message = '\n'.join(http)
    return http_message


if __name__ == '__main__':
    response = Response({'status', 'Account created'}, status=201, content_type='application/json')

    response.set_header('Access-Control', '*')
    response.set_cookie('JWTAuth', 'ey28428377')
    response.set_cookie('sessionId', '34349302')

    http = make_response(response)

    print(http)
