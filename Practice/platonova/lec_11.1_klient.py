import socket

def main():
    host = "127.0.0.1"
    port = 5000

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        words = ["Петр", "Иван", "Федор"]
        data = ",".join(words)
        s.sendall(str(data).encode('utf-8'))
        decrypted_data = s.recv(1024)
        print(decrypted_data.decode("utf-8"))

if __name__ == "__main__":
    main()
