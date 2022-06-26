from types import FunctionType
from functools import wraps


class IPFilter(object):
    _permitted = []

    def add_permitted(self, ip: str) -> None:
        self._permitted.append(ip)

    def ipfilter(self, function: FunctionType) -> FunctionType:
        @wraps(function)
        def wrapper(*args):
            request = args[0]
            if request.host in self._permitted:
                return function(*args)
            else:
                return 'Forbidden', 401

        return wrapper
