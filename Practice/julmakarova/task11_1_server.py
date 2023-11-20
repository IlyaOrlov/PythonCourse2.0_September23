import socket


SERV_DICT = {"hello": "привет", "sorry": "извините", "please": "пожалуйста", "bye": "пока"}


class MyServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self._socket = None

    def run(self):
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self._socket.bind((self.host, self.port))
        self._socket.listen(3)
        print("Сервер готов к подключениям")

        while True:
            conn, addr = self._socket.accept()
            with conn:
                print(f"К серверу подключился {addr}")
                data = conn.recv(1024)
                s_word = data.decode().split()
                s_data = ""
                for i in s_word:
                    if i in SERV_DICT.keys():
                        i = SERV_DICT.get(i)
                    else:
                        i = "(NOT IN THE DICT)"
                    s_data += i + " "
                conn.send(s_data.encode())

    def stop(self):
        self._socket.close()
        print("Сервер отключен")


if __name__ == '__main__':
    server = MyServer(host='127.0.0.1', port=5000)
    try:
        server.run()
    except KeyboardInterrupt:
        server.stop()
