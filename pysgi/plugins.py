from functools import wraps
from types import FunctionType

from .utils.default_responses import DefaultResponses


class IPFilter(object):
    _permitted: list = []

    def add_permitted(self, ip: str) -> None:
        self._permitted.append(ip)

    def ipfilter(self, func: FunctionType) -> FunctionType:
        @wraps(func)
        def wrapper(request):
            host = request.client_host

            if host in self._permitted:
                return func(request)
            else:
                return DefaultResponses.unauthorized
        return wrapper
