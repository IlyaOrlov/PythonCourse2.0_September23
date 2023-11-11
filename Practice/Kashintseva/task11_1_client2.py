import socket


class TcpClient:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self._socket = None

    def run(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as self._socket:
            self._socket.connect((self.host, self.port))
            words = ["Мск", "СПБ", "НН", "Гусь", "Влад"]
            self._socket.send(",".join(words).encode())
            print(f"Список зашифрованных слов направлен")
            d = self._socket.recv(1024)
            print(f'Расшифрованные слова: {d.decode()}')


if __name__ == '__main__':
    myclient = TcpClient(host='127.0.0.1', port=55503)
    myclient.run()
