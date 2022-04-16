from typing import Union
import json


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
        self._body: Union[str, dict, list] = body
        self._status: int = status
        self._content_type: str = content_type

        self._cookies: dict = {}
        self._headers: dict = {}

    def set_cookie(self, name: str, value: str) -> None:
        """Set a cookie"""
        self._cookies[name] = value

    def set_header(self, name: str, value: str) -> None:
        """Set a header"""
        self._headers[name] = value
