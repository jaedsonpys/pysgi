from types import FunctionType

from ._print import print_start
from ._request import Request
from ._sockethandler import SocketHandler
from .route import Route

_server = SocketHandler()
ACCEPTED_METHODS = ['POST', 'GET', 'PUT', 'DELETE', 'PATH']


class PySGI(object):
    routes = {}

    def route(self, path: str, methods: list = ['GET']) -> FunctionType:
        """Adds a new route to the application.

        Pass the "route" argument with the name of
        the route (using "/") and also pass the
        "methods" argument, which is a list.
        In the "methods" argument, you define
        the methods accepted by the route, 
        such as `GET`, `POST`, `PUT` and others.

        :param path: Route name.
        :type path: str
        :param methods: Accepted methods, defaults to ['GET']
        :type methods: list, optional
        :raises TypeError: If the `methods` argument is not a list
        """

        if not isinstance(methods, list):
            raise TypeError(f'A named list of methods is required, not {type(methods)}')

        route = Route()
        route.path = path
        
        for m in methods:
            if m.upper() in ACCEPTED_METHODS:
                route.allowed_methods.append(m)

        if '<' in path and '>' in path:
            self._register_dynamic_route(route, path)

        def wrapper(function: FunctionType):
            route.function = function
            self.routes[path] = route
            return function

        return wrapper

    def _register_dynamic_route(self, route: Route, path: str) -> None:
        split_path = path.split('/')
        
        while '' in split_path:
            split_path.remove('')

        parameters = []
        no_parameters = []

        for index, i in enumerate(split_path):
            if i.startswith('<') and i.endswith('>'):
                i = i.replace('<', '')
                i = i.replace('>', '')
                i = i.replace(' ', '')

                parameter = i.split(':')

                if len(parameter) == 2:
                    var_type, name = parameter
                else:
                    var_type = 'any'
                    name = i

                parameters.append({'index': index, 'var_type': var_type, 'name': name})
            else:
                no_parameters.append({'index': index, 'name': i})

        # register registering dynamic route variables
        route.parameters = parameters
        route.no_parameters = no_parameters

    def run(self, host: str = None, port: str = None) -> None:
        """Starts the server on the specified host
        and port (or not).

        It is in this method that the server
        starts waiting for connections and
        starting threads to handle requests.

        :param host: _description_, defaults to '127.0.0.1'
        :type host: str, optional
        :param port: _description_, defaults to 5500
        :type port: str, optional
        """

        address = _server.create_socket(host=host, port=port)
        request = Request(self.routes)

        print_start(*address)

        try:
            while True:
                client = _server.wait_connection()
                request.handle_request(client)
        except KeyboardInterrupt:
            _server.close_server()
