import socket


class TcpClient:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self._socket = None

    def run(self):
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._socket.connect((self.host, self.port))
        words = input("введи слова: ")
        self._socket.send(words.encode())
        r_words = self._socket.recv(1024)
        print('Received: {}'.format(r_words.decode()))
        self._socket.close()


if __name__ == '__main__':
    my_client = TcpClient(host='127.0.0.1', port=5555)
    my_client.run()
