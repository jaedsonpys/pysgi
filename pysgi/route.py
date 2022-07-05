from types import FunctionType

class Route(object):
    def __init__(self) -> None:
        self.function: FunctionType = None
        self.allowed_methods: list = []
        self.parameters: list = []
        self.no_parameters: list = []
        self.path: str = None

    def __repr__(self) -> str:
        """
        @return: str
        """
        return (
            f"Route(function={self.function}, allowed_methods={self.allowed_methods}, " \
            f"path={self.path}, parameters={self.parameters}, no_parameters={self.no_parameters})"
        )

    def __eq__(self, other: object) -> bool:
        """
        @param other: object
        @return: bool
        """
        if isinstance(other, Route):
            return (
                self.function == other.function and
                self.allowed_methods == other.allowed_methods and
                self.path == other.path and
                self.parameters == other.parameters and
                self.no_parameters == other.no_parameters
            )
        return False
