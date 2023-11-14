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

    def receive_message(self):
        data = []
        while True:
            x = self._socket.recv(4096)
            if not x:
                break
            data.append(x)
            message = pickle.loads(b''.join(data))
            return message

    def __del__(self):
        self._socket.close()


if __name__ == "__main__":
    client = MyClient(host='127.0.0.1', port=6000)
    client.connect()
    name = input('Введите имя пользователя: ')
    age = input('Введите возраст пользователя: ')
    new_user = User(name, age)
    client.send_user(new_user)
    response = client.receive_message()
    print(response)
