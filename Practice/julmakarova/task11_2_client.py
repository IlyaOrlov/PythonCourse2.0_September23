import socket
import pickle
from task11_2_user import User


class ClientUser:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self._socket = None

    def run(self):
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        with self._socket as s:
            s.connect((self.host, self.port))
            cl_user = User(input("Введите имя: "), input("Введите возраст: "))
            s.send(pickle.dumps(cl_user))
            print(s.recv(1024).decode())


if __name__ == "__main__":
    client = ClientUser(host='127.0.0.1', port=5432)
    client.run()
