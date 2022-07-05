from datetime import datetime

def print_response(status: int, path: str, method: str, host: str) -> str:
    time = datetime.now()
    statusCode = {
        400: f'* [{time}][\033[1;31m{status}\033[m] {host}: ({method}) {path}',
        300: f'* [{time}][\033[1;33m{status}\033[m] {host}: ({method}) {path}',
        200: f'* [{time}][\033[1;32m{status}\033[m] {host}: ({method}) {path}',
    }
    for key, value in statusCode.items():
        if status >= key:
            print(value)
