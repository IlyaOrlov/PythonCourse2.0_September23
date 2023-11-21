import socket
import pickle


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    host = '127.0.0.1'
    port = 12345
    s.connect((host, port))
    client_words_shifr = ['ВМГП', 'ЗОТИ', 'ОД', 'УЗМС']
    s.send(pickle.dumps(client_words_shifr))
    print("Отправлен список зашифрованных слов:", client_words_shifr)
    print("Получен список расшифрованных слов:", pickle.loads(s.recv(1024)))
