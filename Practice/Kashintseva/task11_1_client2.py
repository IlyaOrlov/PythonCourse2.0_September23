import socket


class TcpClient:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self._socket = None

    def run(self):
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._socket.connect((self.host, self.port))
        words = ["Мск", "СПБ", "НН", "Гусь"]
        self._socket.send(",".join(words).encode())
        print(f"Список зашифрованных слов направлен")
        d = self._socket.recv(1024)
        print(f'Расшифрованные слова: {d.decode()}')
        self._socket.close()


if __name__ == '__main__':
    myclient = TcpClient(host='127.0.0.1', port=55503)
    myclient.run()
