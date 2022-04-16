from datetime import datetime


def print_start(host: str, port: int) -> None:
    print(f'\033[1m@PySGI Server\033[m')
    print(f'\033[4;47;35mRunning in http://{host}:{port}\033[m\n')


def print_response(status: int, path: str, method: str, host: str) -> None:
    time = datetime.now()

    if status >= 400:print(f'* [{time}][\033[1;31m{status}\033[m] {host}: ({method}) {path}')
    elif status >= 300: print(f'* [{time}][\033[1;33m{status}\033[m] {host}: ({method}) {path}')
    elif status >= 200: print(f'* [{time}][\033[1;32m{status}\033[m] {host}: ({method}) {path}')
