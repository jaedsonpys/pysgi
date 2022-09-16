from datetime import datetime


def print_start(host: str, port: int) -> None:
    print('\033[4;32mPySGI application server started\033[m\n')
    print('»» Learn more about the server at \033[4mgithub.com/jaedsonpys/pysgi\033[m')
    print(f'»» Running in http://{host}:{port}\n')


def print_response(status: int, path: str, method: str, host: str) -> None:
    time = datetime.now()

    status_code = {
        400: f'» [\033[33m{time}\033[m][{host}] \033[1;31m{status}\033[m {path} ({method})',
        300: f'» [\033[33m{time}\033[m][{host}] \033[1;33m{status}\033[m {path} ({method})',
        200: f'» [\033[33m{time}\033[m][{host}] \033[1;32m{status}\033[m {path} ({method})',
    }

    for key, value in status_code.items():
        if status >= key:
            print(value)
            break
