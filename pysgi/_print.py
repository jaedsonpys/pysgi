from datetime import datetime
from .__init__ import __version__


def print_start(host: str, port: int) -> None:
    print(f'\033[1m@PySGI Server ({__version__})\033[m')
    print(f'\033[4;47;35mRunning in http://{host}:{port}\033[m\n')


def print_request(path: str, method: str, host: str) -> None:
    time = datetime.now()
    print(f'   * [{time}] {host}: ({method} {path})')
