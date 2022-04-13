# the "_sockethandler" file is responsible for
# handling the TCP connections from the socket.

import socket
import os

LISTEN_MAX = 128


class SocketHandler(object):
    def __init__(self, use_environ: bool = False) -> None:
        self._socket: socket.SocketIO

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
        self._socket.setblocking(False)

        self._socket.bind(address)
        self._socket.listen(LISTEN_MAX)
