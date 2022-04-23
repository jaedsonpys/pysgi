from types import FunctionType


class Route(object):
    function: FunctionType = None
    allowed_methods: list = []
    parameters: list = []
    path: str = None

    def __repr__(self) -> str:
        return f'Route(function={self.function}, allowed_methods={self.allowed_methods}, ' \
               f'path={self.path}, dynamics={self.dynamics})'
