import socket
import pickle


class MyClient:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self._socket = None

    def connect_server(self, encrypted_words):
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self._socket.connect((self.host, self.port))
            print('Соединение с сервером установлено')
            data = pickle.dumps(encrypted_words)
            self._socket.send(data)
            response = self._socket.recv(1024)
            decrypted_words = pickle.loads(response)
            return decrypted_words
        except Exception as e:
            print(f"Ошибка при работе с сервером: {e}")
        finally:
            self._socket.close()


if __name__ == "__main__":
    client = MyClient(host='127.0.0.1', port=5000)
    try:
        my_encrypted_words = [input("Введите слова через пробел: ")]
        my_decrypted_words = client.connect_server(my_encrypted_words)
        print("Полученный список расшифрованных слов:")
        for word in my_decrypted_words:
            print(word)
    except Exception as x:
        print('Ошибка при работе с клиентом:', x)
