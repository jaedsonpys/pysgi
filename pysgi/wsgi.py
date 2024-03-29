import sys
from types import FunctionType
from threading import Thread

from ._request import Request
from ._sockethandler import SocketHandler
from .route import Route
from .utils._print import print_start


class PySGI(object):
    def __init__(self) -> None:
        self._server = SocketHandler()
        self._routes = {}

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

        new_route = Route()

        new_route.path = path
        new_route.allowed_methods = [m.upper() for m in methods]

        if '<' in path and '>' in path:
            self._register_dynamic_route(new_route, path)

        def decorator(func):
            new_route.function = func
            self._routes[path] = new_route
            return func

        return decorator

    def _register_dynamic_route(self, route: Route, path: str) -> None:
        split_path = path.split('/')        
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

    def run(self, host: str = '127.0.0.1', port: int = 5500) -> None:
        """Starts the server on the specified host
        and port (or not).

        It is in this method that the server
        starts waiting for connections and
        starting threads to handle requests.

        :param host: Host, defaults to '127.0.0.1'
        :type host: str, optional
        :param port: Port, defaults to 5500
        :type port: str, optional
        """

        try:
            address = self._server.create_socket(host=host, port=port)
        except OSError:
            print(f'\033[31m* ERROR: The server cannot be started at {host}:{port}.\n  '
                   'Check if there are any services \033[4mrunning at this address\033[m\033[31m and try again.\033[m')

            sys.exit(1)

        print_start(*address)

        try:
            while True:
                client = self._server.wait_connection()
                request = Request(client, self._routes)

                th = Thread(target=request.handle_request)
                th.setDaemon(True)
                th.start()
        except (KeyboardInterrupt, SystemExit, SystemError):
            self._server.close_server()
            sys.exit(0)
