from types import FunctionType

from _request import parser_http
from _sockethandler import SocketHandler
from route import Route

socket = SocketHandler()
routes = {}


class PySGI(object):
    def route(self, path: str, methods: list = ['GET']) -> FunctionType:
        route = Route()
        route.path = path
        route.allowed_methods = methods

        def _decorator_func(function: FunctionType):
            route.function = function
            routes[path] = route
            return function

        return _decorator_func
