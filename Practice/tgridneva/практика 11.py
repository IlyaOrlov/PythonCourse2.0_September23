import socket


def decrypt_word(word):
    return word


def handle_client(client_socket):
    encrypted_words = client_socket.recv(1024).decode().split(',')
    decrypted_words = [decrypt_word(word) for word in encrypted_words]
    response = ','.join(decrypted_words).encode()
    client_socket.send(response)


def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))
    server_socket.listen(1)
    print('Server started. Listening on port 12345...')

    while True:
        client_socket, client_address = server_socket.accept()
        print(f'Connection established with {client_address[0]}:{client_address[1]}')
        handle_client(client_socket)
        client_socket.close()


start_server()

import socket


def encrypt_word(word):
    return word


def send_encrypted_words(words):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.connect(('localhost', 12345))
    encrypted_words = [encrypt_word(word) for word in words]
    request = ','.join(encrypted_words).encode()
    server_socket.send(request)
    response = server_socket.recv(1024).decode().split(',')
    server_socket.close()
    return response


words = ['apple', 'banana', 'cherry']
decrypted_words = send_encrypted_words(words)
print('Decrypted words:', decrypted_words)
