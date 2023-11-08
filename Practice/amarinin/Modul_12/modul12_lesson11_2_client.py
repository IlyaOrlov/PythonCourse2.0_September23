import socket
import pickle
import User


if __name__ == "__main__":
    while True:
        name = input("Введите имя пользователя     : ")
        age = input("Введите возраст пользователя : ")
        if not len(name) or not len(age):
            break
        user = User.User(name, age)
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            host = '127.0.0.1'
            port = 12345
            s.connect((host, port))
            s.send(pickle.dumps(user))
