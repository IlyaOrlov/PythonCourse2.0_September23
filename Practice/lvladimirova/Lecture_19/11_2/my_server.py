import socket
import pickle


class MyServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self._socket = None
        self.users_list = []

    def start_server(self):
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self._socket.bind((self.host, self.port))
        self._socket.listen(5)
        print('Сервер запущен')

        while True:
            conn, addr = self._socket.accept()
            print(f"Получен запрос на соединение от: {addr}")
            with conn:
                user_info_data = conn.recv(1024)
                user_info = pickle.loads(user_info_data)
                print(f"Подключённый пользователь: {user_info.name}")
                self.users_list.append(user_info)
                conn.close()

    def stop(self):
        self._socket.close()
        print("Сервер отключен")

    def __del__(self):
        self._socket.close()


if __name__ == '__main__':
    server = MyServer(host='127.0.0.1', port=5000)
    try:
        server.start_server()
    except KeyboardInterrupt:
        server.stop()
