from datetime import datetime


def print_start(host: str, port: int) -> str:
    print(f'\033[1m@PySGI Server\033[m')
    print(f'\033[4;47;35mRunning in http://{host}:{port}\033[m\n')


def print_response(status: int, path: str, method: str, host: str) -> str:
    time = datetime.now()
    status_code = {
        400: f'* [{time}][\033[1;31m{status}\033[m] {host}: ({method}) {path}',
        300: f'* [{time}][\033[1;33m{status}\033[m] {host}: ({method}) {path}',
        200: f'* [{time}][\033[1;32m{status}\033[m] {host}: ({method}) {path}',
    }
    for key, value in status_code.items():
        if status >= key:
            print(value)
