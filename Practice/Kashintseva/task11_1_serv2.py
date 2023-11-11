import socket


class TcpServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self._socket = None
        self._running = False

    def run(self):
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self._socket.bind((self.host, self.port))
        self._socket.listen(5)
        self._running = True

        print("Сервер запущен")
        sh = {"Мск": "Москва", "НН": "Нижний Новгород", "Гусь": "Гусь-Хрустальный", "СПБ": "Санкт-Петербург"}
        while self._running:
            conn, addr = self._socket.accept()
            with conn:
                print(f"Подключение установилось c адреса {addr}. Ждем список слов.")
                c = conn.recv(1024).decode().split(",")
                c1 = ""
                for i in c:
                    if i in sh:
                        c1 += sh[i] + ", "
                    else:
                        c1 += "введено что-то неизвестное"
                conn.send(c1.encode())
                print(f"Список расшифрованных слов направлен.")

    def stop(self):
        self._running = False
        self._socket.close()
        print("Сервер завершил работу")


if __name__ == '__main__':
    srv = TcpServer(host='127.0.0.1', port=55503)
    try:
        srv.run()
    except KeyboardInterrupt:
        srv.stop()
