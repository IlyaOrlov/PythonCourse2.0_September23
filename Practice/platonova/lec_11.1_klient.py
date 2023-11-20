import socket

def main():
    host = "127.0.0.1"
    port = 5000

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        words = ["xlmw", "qeb", "livi"]
        data = ",".join(words)
        s.sendall(str.encode(data))
        decrypted_data = s.recv(1024)
        print(decrypted_data.decode("utf-8"))

if __name__ == "__main__":
    main()
