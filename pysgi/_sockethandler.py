# the "_sockethandler" file is responsible for
# handling the TCP connections from the socket.

import socket


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
        return f'Client(csocket={self.csocket}, host={self.host}, port={self.port})'

class SocketHandler(object):
    def __init__(self) -> None:
        self._socket: socket.socket
        self._listen_max = 128

    def create_socket(self, host: str = None, port: int = None) -> tuple:        
        address = (host, port)

        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        self._socket.bind(address)
        self._socket.listen(self._listen_max)

        return address

    def wait_connection(self) -> Client:
        client_socket, addr = self._socket.accept()
        return Client(client_socket, *addr)

    def send_response(client: Client, response: bytes) -> None:
        client.csocket.send(response)

    def close_server(self) -> None:
        self._socket.shutdown(socket.SHUT_RDWR)
        self._socket.close()
