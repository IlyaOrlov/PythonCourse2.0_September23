import socket
import pickle

def decrypt_words(encrypted_words):
    dictionary = {
        'par**': 'Paris',
        'is***bul': 'Istanbul',
        'Li**on': 'Lisbon',
        'lon**n': 'London'
    }
    decrypted_words = []

    for word in encrypted_words:
        decrypted_word = dictionary.get(word)
        decrypted_words.append(decrypted_word)

    return decrypted_words


def handle_client(conn):
    recv_data = conn.recv(1024)

    encrypted_words = pickle.loads(recv_data)

    decrypted_words = decrypt_words(encrypted_words)

    send_data = pickle.dumps(decrypted_words)

    conn.sendall(send_data)

    conn.close()


def start_server():
    host = 'mynet'
    port = 13579

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()

        print("Server started.")

        while True:
            conn, addr = s.accept()
            print(f"Client connected: {addr}")

            handle_client(conn)


if __name__ == "__main__":
    start_server()