# the "_sockethandler" file is responsible for
# handling the TCP connections from the socket.

import socket
import os
from typing import Tuple

LISTEN_MAX = 128


class Client(object):
    socket: socket.socket
    message: str
    host: str
    port: int

    def __init__(
        self,
        _socket: socket.socket,
        host: str,
        port: int,
        message: str
    ) -> None:
        self.socket = _socket
        self.host = host
        self.port = port
        self.message = message

    def __repr__(self) -> str:
        return f'ClientSocket(socket={self.socket}, address={self.address}, message={self.message}'


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

    def create_socket(self) -> None:
        address = (self._host, self._port)

        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._socket.bind(address)
        self._socket.listen(LISTEN_MAX)

    def wait_connection(self) -> Client:
        client_socket, addr = self._socket.accept()
        client_socket.settimeout(2)

        try:
            client_msg = client_socket.recv(1024)
        except socket.timeout:
            client_socket.close()
        else:
            client_socket.settimeout(None)

        client = Client(client_socket, addr, client_msg)
        return client
