import socket


class TcpClient:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self._socket = None

    def run(self):
        while d := input("Введите id детали: "):
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as self._socket:
                self._socket.connect((self.host, self.port))
                self._socket.send(d.encode())
                res = self._socket.recv(1024)
                print(f'Detail info: {res.decode()}')


if __name__ == '__main__':
    myclient = TcpClient(host='127.0.0.1', port=5555)
    myclient.run()