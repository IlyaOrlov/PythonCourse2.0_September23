import socket
import pickle


class MyServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self._socket = None

    @staticmethod
    def decrypt_words(encrypted_words):
        decrypted_words = []
        for word in encrypted_words:
            decrypted_word = word[::-1]
            decrypted_words.append(decrypted_word)
        return decrypted_words

    def start_server(self):
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self._socket.bind((self.host, self.port))
        self._socket.listen(5)
        print('Сервер запущен')

        while True:
            try:
                conn, addr = self._socket.accept()
                print(f"Получен запрос на соединение от: {addr}")
                with conn:
                    data = conn.recv(1024)
                    encrypted_words = pickle.loads(data)
                    decrypted_words = self.decrypt_words(encrypted_words)
                    data = pickle.dumps(decrypted_words)
                    conn.send(data)
            except Exception as e:
                print('Ошибка соединения с клиентом:', e)

    def stop(self):
        self._socket.close()
        print("Сервер выключен")


if __name__ == '__main__':
    server = MyServer(host='127.0.0.1', port=5000)
    try:
        server.start_server()
    except KeyboardInterrupt:
        server.stop()
