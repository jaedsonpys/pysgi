# this file has all the code that handles
# requests coming from a client.

from socket import timeout as sock_timeout
from types import FunctionType
from typing import Tuple

import http_pyparser

from ._sockethandler import Client
from .response import Response, make_response
from .route import Route
from .utils._print import print_response
from .utils.default_responses import DefaultResponses


class Request(object):
    def __init__(self, client: Client, routes: dict[Route]) -> None:
        self._routes = routes
        self._client = client

    def _get_route_parameters(self, path_split: list, parameters: dict) -> dict:
        result = {}
        
        for d in parameters:
            index = d['index']
            var_type = d['var_type']
            name = d['name']

            variable = path_split[index]
            
            if var_type == 'str':
                variable = str(variable)
            elif var_type == 'int':
                variable = int(variable)
            elif var_type == 'float':
                variable = float(variable)

            result[name] = variable

        return result

    def _get_route(self, path: str) -> Tuple[Route, dict]:
        path_split = path.split('/')

        while '' in path_split:
            path_split.remove('')

        for route in self._routes.values():
            route_find = False

            if path == route.path:
                return (route, {})
            elif len(path_split) == (len(route.parameters) + len(route.no_parameters)):
                # checking if routes that are not parameters are available
                for a in route.no_parameters:
                    if path_split[a['index']] == a['name']:
                        route_find = True
                    else:
                        route_find = False
                        break

                # if the route was found get its arguments
                if route_find:
                    return (route, self._get_route_parameters(path_split, route.parameters))
        
        return None, None

    def handle_request(self) -> None:
        self._client.csocket.settimeout(2.5)

        try:
            client_msg = self._client.csocket.recv(1024)
        except sock_timeout:
            # in this situation, the client has not
            # sent any message to the server, and
            # therefore its request cannot be processed,
            # closing the connection with the client
            # without returning anything.
            
            self._client.csocket.close()
            return None
        else:
            self._client.csocket.settimeout(None)
            
        parser = http_pyparser.HTTPParser()

        try:
            request = parser.parser(client_msg.decode())
        except http_pyparser.exceptions.InvalidHTTPMessageError:
            return self._send_response(self._client, DefaultResponses.bad_request)

        requested_route, parameters = self._get_route(request.path)

        request.parameters = parameters
        request.client_host = self._client.host

        # if the route is not found
        if not requested_route:
            response = DefaultResponses.not_found
        else:
            if request.method not in requested_route.allowed_methods:
                response = DefaultResponses.method_not_allowed
            else:
                route_function: FunctionType = requested_route.function

                try:
                    function_response = route_function.__call__(request)
                except TypeError:
                    function_response = route_function.__call__()

                if isinstance(function_response, tuple):
                    # getting body and status of response 
                    # in use cases of: return "Hello", 200.
                    body, status = function_response
                    response = Response(body, status=status)
                elif isinstance(function_response, str):
                    response = Response(function_response)
                elif isinstance(function_response, Response):
                    response = function_response

        self._send_response(response)
        print_response(response.status, request.real_path, request.method, self._client.host)

    def _send_response(self, response: Response) -> None:
        http_response = make_response(response)
        self._client.csocket.send(http_response.encode())
        self._client.csocket.close()
