import socket

def decrypt_words(words):
    dictionary = {"xlmw": "word1", "qeb": "word2", "livi": "word3"}
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
                conn.sendall(str.encode(",".join(decrypted_words)))

if __name__ == "__main__":
    main()
