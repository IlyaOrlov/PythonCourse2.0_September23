import socket


if __name__ == "__main__":
    while True:
        secret = input("введите через пробел секретые слова ABRA KADABRA BAZZ  :")
        if not len(secret):
            break
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            host = '127.0.0.1'
            port = 12345
            s.connect((host, port))
            s.send(secret.encode())
            print(s.recv(1024).decode()[1:-1].replace(",", "").replace("'", ""))
