import socket


if __name__ == "__main__":
    secret_data = {"abra": "super", "kadabra": "evrika", "bazz": "brilliantly"}
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        host = '127.0.0.1'
        port = 12345
        s.bind((host, port))
        s.listen(5)
        while True:
            print("Жду клиента")
            conn, addr = s.accept()
            with conn:
                print(f'Server got connection from {addr}')
                d_in = conn.recv(1024).decode().strip().lower().split()
                d_out = [secret_data[i] for i in d_in if i in secret_data]
                conn.send(str(d_out).encode() if len(d_out) else "ничего секретного".encode())
                print("Отправил клиенту")
