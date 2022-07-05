from types import FunctionType
from functools import wraps

class IPFilter(object):
    _permitted: list = []

    def add_permitted(self, ip: str) -> None:
        self._permitted.append(ip)

    def ipfilter(self, func: FunctionType) -> FunctionType:
        @wraps(func)
        def wrapper(*args, **kwargs):
            request = args[0]
            if request.host in self._permitted:
                return func(*args, **kwargs)
            else:
                return "Unauthorized", 401
        return wrapper
