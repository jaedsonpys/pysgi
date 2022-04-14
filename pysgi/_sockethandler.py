# the "_sockethandler" file is responsible for
# handling the TCP connections from the socket.

import socket
import os

LISTEN_MAX = 128


class Client(object):
    """The Client class is used to store
    the connection information of a client,
    such as its socket, host, port and the
    message that was sent by it.
    """

    csocket: socket.socket
    host: str
    port: int

    def __init__(
        self,
        _socket: socket.socket,
        host: str,
        port: int,
    ) -> None:
        self.csocket = _socket
        self.host = host
        self.port = port

    def __repr__(self) -> str:
        return f'ClientSocket(socket={self.csocket}, address=({self.host, self.port}))'


class SocketHandler(object):
    def __init__(self, use_environ: bool = False) -> None:
        self._socket: socket.socket

        self._host = '127.0.0.1'
        self._port = 5500

        if use_environ:
            env_host = os.getenv('PYSGI_HOST')
            env_port = os.getenv('PYSGI_PORT')

            if env_host: self._host = env_host
            if env_port: self._port = env_port

    def create_socket(self, host: str = None, port: int = None) -> tuple:
        _host = host if host else self._host
        _port = port if port else self._port

        address = (_host, _port)

        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        self._socket.bind(address)
        self._socket.listen(LISTEN_MAX)

        return address

    def wait_connection(self) -> Client:
        client_socket, addr = self._socket.accept()

        _host = addr[0]
        _port = addr[1]

        client = Client(client_socket, _host, _port)
        return client

    def send_response(client: Client, response: bytes) -> None:
        client.csocket.send(response)

    def close_server(self) -> None:
        self._socket.shutdown(socket.SHUT_RDWR)
        self._socket.close()


if __name__ == '__main__':
    server = SocketHandler()
    server.create_socket()

    client = server.wait_connection()
    print(f'client {client.host} connected')

    client.csocket.send(b'HTTP/1.1 200 OK\n\nHello!')
