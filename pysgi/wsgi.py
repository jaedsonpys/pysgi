from types import FunctionType

from ._print import print_request, print_start
from ._request import Request
from ._sockethandler import SocketHandler
from .route import Route

_server = SocketHandler()
routes = {}


class PySGI(object):
    def route(self, path: str, methods: list = ['GET']) -> FunctionType:
        if not isinstance(methods, list):
            raise TypeError(f'A named list of methods is required, not {type(methods)}')

        route = Route()
        route.path = path
        route.allowed_methods = methods

        def _decorator_func(function: FunctionType):
            route.function = function
            routes[path] = route
            return function

        return _decorator_func

    def run(self, host: str = None, port: str = None) -> None:
        address = _server.create_socket(host=host, port=port)
        request = Request(routes)

        print_start(*address)

        try:
            while True:
                client = _server.wait_connection()
                request.handle_request(client)
        except KeyboardInterrupt:
            _server.close_server()
