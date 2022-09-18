import json
from socket import timeout as sock_timeout
from types import FunctionType
from typing import Tuple, Union

import http_pyparser

from ._sockethandler import Client
from .response import Response, make_response
from .route import Route
from .utils._print import print_response
from .utils.default_responses import DefaultResponses


class RequestData(object):
    def __init__(
        self,
        http_data: http_pyparser.HTTPData,
        parameters: dict,
        client_host: str
    ) -> None:
        self.real_path = http_data.real_path

        self.path = http_data.path
        self.method = http_data.method
        self.version = http_data.version
        
        self.user_agent = http_data.user_agent
        self.accept = http_data.accept
        self.body = http_data.body

        self.query = http_data.query
        self.headers = http_data.headers
        self.cookies = http_data.cookies

        self.host = client_host
        self.parameters = parameters

    def json(self) -> Union[None, dict]:
        """Return body as JSON.

        If None is returned, it means that the request
        does not have a body.

        This method does not handle exceptions,
        decoding errors will be thrown by the `json` module

        :return: Body as JSON format
        :rtype: Union[None, dict]
        """

        if self.body:
            data = json.loads(self.body)
        else:
            data = None

        return data

    def __repr__(self) -> str:
        return (f'RequestData(real_path="{self.real_path}", path="{self.path}", method="{self.method}", '
                f'version="{self.version}", host="{self.host}", user_agent="{self.user_agent}", '
                f'accept="{self.accept}", body={self.body}, headers={self.headers}, '
                f'cookies={self.cookies}, query={self.query}, parameters={self.parameters})')


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

    def _get_client_data(self) -> Union[str, None]:
        self._client.csocket.settimeout(2.5)

        try:
            client_msg = self._client.csocket.recv(1024)
        except sock_timeout:
            return None

        self._client.csocket.settimeout(None)
        return client_msg.decode()

    def _get_route_response(self, function: FunctionType, request: RequestData) -> Response:
        try:
            route_response = function.__call__(request)
        except TypeError:
            route_response = function.__call__()

        if isinstance(route_response, tuple):
            # getting body and status of response 
            # in use cases of: return "Hello", 200.
            body, status = route_response
            response = Response(body, status=status)
        elif isinstance(route_response, Response):
            response = route_response
        else:
            response = Response(route_response)

        return response

    def handle_request(self) -> None:
        client_msg = self._get_client_data()

        if not client_msg:
            # the client has not sent anything, so it is an invalid request.
            self._client.csocket.close()
            return None

        parser = http_pyparser.HTTPParser()

        try:
            parsed_http = parser.parser(client_msg)
        except http_pyparser.exceptions.InvalidHTTPMessageError:
            return self._send_response(DefaultResponses.bad_request)

        requested_route, parameters = self._get_route(parsed_http.path)
        request = RequestData(parsed_http, parameters, self._client.host)

        # if the route is not found
        if not requested_route:
            response = DefaultResponses.not_found
        else:

            if request.method not in requested_route.allowed_methods:
                response = DefaultResponses.method_not_allowed
            else:
                route_function = requested_route.function
                response = self._get_route_response(route_function, request)

        self._send_response(response)
        print_response(response.status, request.real_path, request.method, self._client.host)

    def _send_response(self, response: Response) -> None:
        http_response = make_response(response)
        self._client.csocket.send(http_response.encode())
        self._client.csocket.close()
