import socket
import pickle
from user import User


class MyClient:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self._socket = None

    def connect(self):
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._socket.connect((self.host, self.port))
        print('Подключение к серверу установлено')

    def send_user(self, user):
        data = pickle.dumps(user)
        self._socket.send(data)

    def __del__(self):
        self._socket.close()


if __name__ == "__main__":
    client = MyClient(host='127.0.0.1', port=5000)
    client.connect()
    name = input('Введите имя пользователя: ')
    age = input('Введите возраст пользователя: ')
    new_user = User(name, age)
    client.send_user(new_user)

