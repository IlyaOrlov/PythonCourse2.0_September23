import threading
import socket
import dbclient


class ClientThread(threading.Thread):
    def __init__(self, conn, addr, dbname):
        super().__init__()
        self._connection = conn
        self._address = addr
        self._dbname = dbname

    def run(self):
        data = self._connection.recv(1024)
        detail_id = int(data.decode())
        with dbclient.DBClient(self._dbname) as db_client:
            res = db_client.get_detail(detail_id)
            if res:
                response = str(res)
            else:
                response = "Такой детали нет"
        self._connection.send(response.encode())

    def __del__(self):
        self._connection.close()


class TcpServer:
    def __init__(self, host, port, dbname):
        self.host = host
        self.port = port
        self._socket = None
        self._running = False
        self._dbname = dbname

    def run(self):
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self._socket.bind((self.host, self.port))
        self._socket.listen(5)
        self._running = True

        print('Server is up')
        while self._running:
            conn, addr = self._socket.accept()
            ClientThread(conn, addr, self._dbname).start()

    def stop(self):
        self._running = False
        self._socket.close()
        print('Server is down')


if __name__ == '__main__':
    srv = TcpServer(host='127.0.0.1', port=5555, dbname="mydetails.db")
    try:
        srv.run()
    except KeyboardInterrupt:
        srv.stop()

