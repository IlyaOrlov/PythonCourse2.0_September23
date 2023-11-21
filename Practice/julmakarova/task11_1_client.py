import socket


class MyClient:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self._socket = None

    def run(self):
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._socket.connect((self.host, self.port))
        data = input("Введите пожалуйста интересующие слова (через пробел): ")
        self._socket.send(data.encode())
        r_data = self._socket.recv(1024)
        print(f"{r_data.decode()}")
        self._socket.close()


if __name__ == "__main__":
    client = MyClient(host='127.0.0.1', port=5000)
    client.run()
