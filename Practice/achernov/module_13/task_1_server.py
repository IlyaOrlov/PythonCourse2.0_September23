import socket


my_dict = {"python": "питон", "very": "очень", "like": "нравится"}


class TcpServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self._socket = None
        self._runnning = False

    def run(self):
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self._socket.bind((self.host, self.port))
        self._socket.listen(5)
        self._runnning = True
        print('Server is up')

        while True:
            conn, addr = self._socket.accept()
            with conn:
                print(f"К серверу подключился {addr}")
                data = conn.recv(1024)
                s_word = data.decode().split()
                s_data = ""
                for k in s_word:
                    if k in my_dict.keys():
                        k = my_dict.get(k)
                    else:
                        k = "(NOT IN THE DICT)"
                    s_data += k + " "
                conn.send(s_data.encode())

    def stop(self):
        self._runnning = False
        self._socket.close()
        print('Server is down')


if __name__ == '__main__':
    srv = TcpServer(host='127.0.0.1', port=5555)
    try:
        srv.run()
    except KeyboardInterrupt:
        srv.stop()
