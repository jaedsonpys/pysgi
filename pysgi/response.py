from typing import Union

SERVER_NAME = 'PySGI'


class Response(object):
    """This class stores information from
    the response created by the function
    responsible for a route.
    """

    def __init__(
        self,
        body: Union[str, dict, list],
        status: int = 200,
        content_type: str = 'text/html',
    ) -> None:
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
