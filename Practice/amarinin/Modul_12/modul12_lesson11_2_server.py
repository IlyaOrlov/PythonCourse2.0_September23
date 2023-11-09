import socket
import pickle
import User


if __name__ == "__main__":
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        host = '127.0.0.1'
        port = 12345
        s.bind((host, port))
        s.listen(5)
        while True:
            print("Жду Users")
            conn, addr = s.accept()
            with conn:
                print(pickle.loads(conn.recv(1024)))
