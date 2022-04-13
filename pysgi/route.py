from types import FunctionType


class Route(object):
    function: FunctionType
    allowed_methods: list
    path: str

    def __repr__(self) -> str:
        return f'Route(function={self.function}, allowed_methods={self.allowed_methods}\
                path={self.path})'
