import socket
import pickle


class MyServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self._socket = None

    def start_server(self):
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self._socket.bind((self.host, self.port))
        self._socket.listen(5)
        print('Сервер запущен')

        while True:
            try:
                connected_users = []
                conn, addr = self._socket.accept()
                print(f"Получен запрос на соединение от: {addr}")
                with conn:
                    data = conn.recv(1024)
                    user = pickle.loads(data)
                    connected_users.append(user)
                    for user in connected_users:
                        print(user)
                    message = f'Добро пожаловать, {user.name}!'
                    response = pickle.dumps(message)
                    conn.send(response)
            except Exception as e:
                print('Ошибка при работе с клиентом:', e)

    def stop(self):
        self._socket.close()
        print("Сервер отключен")

    def __del__(self):
        self._socket.close()


if __name__ == '__main__':
    server = MyServer(host='127.0.0.1', port=6000)
    try:
        server.start_server()
    except KeyboardInterrupt:
        server.stop()
