import socket

def decrypt_words(words):
    dictionary = {"Петр": "Peter", "Иван": "Ivan", "Федор": "Theodore"}
    decrypted = [dictionary.get(word, "Unknown") for word in words]
    return decrypted

def main():
    host = "127.0.0.1"
    port = 5000

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                words = data.decode("utf-8").split(",")
                decrypted_words = decrypt_words(words)
                conn.sendall(str(",".join(decrypted_words)).encode('utf-8'))

if __name__ == "__main__":
    main()
