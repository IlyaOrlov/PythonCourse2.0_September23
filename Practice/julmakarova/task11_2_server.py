import socket
import pickle
from task11_2_user import User


class ServerForUser:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self._socket = None

    def run(self):
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self._socket.bind((self.host, self.port))
        self._socket.listen(5)
        print("Сервер готов к подключениям")

        while True:
            conn, addr = self._socket.accept()
            with conn:
                data = conn.recv(1024)
                print(pickle.loads(data))
                r_mes = "Спасибо за подключение!"
                conn.send(r_mes.encode())

    def stop(self):
        self._socket.close()
        print("Сервер отключен")


if __name__ == '__main__':
    server = ServerForUser(host='127.0.0.1', port=5432)
    try:
        server.run()
    except KeyboardInterrupt:
        server.stop()
