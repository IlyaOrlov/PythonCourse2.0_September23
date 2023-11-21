import socket
import pickle
import user


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    host = '127.0.0.1'
    port = 12345
    s.connect((host, port))  # подключаемся к серверу
    print(pickle.loads(s.recv(1024)))  # получаем и выводим данные, полученные от сервера
