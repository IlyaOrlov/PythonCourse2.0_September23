import socket


def decrypt_word(word):
    return word


def handle_client(client_socket):
    encrypted_words = client_socket.recv(1024).decode().split(',')
    decrypted_words = [decrypt_word(word) for word in encrypted_words]
    response = ','.join(decrypted_words).encode()
    client_socket.send(response)


def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind(('localhost', 12345))
        server_socket.listen(1)
        print('Server started. Listening on port 12345...')

        while True:
            client_socket, client_address = server_socket.accept()
            with client_socket:
                print(f'Connection established with {client_address[0]}:{client_address[1]}')
                handle_client(client_socket)


if __name__ == '__main__':
    start_server()
