import socket


def encrypt_word(word):
    return word


def send_encrypted_words(words):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.connect(('localhost', 12345))
        encrypted_words = [encrypt_word(word) for word in words]
        request = ','.join(encrypted_words).encode()
        server_socket.send(request)
        response = server_socket.recv(1024).decode().split(',')
        return response


if __name__ == '__main__':
    words = ['apple', 'banana', 'cherry']
    decrypted_words = send_encrypted_words(words)
    print('Decrypted words:', decrypted_words)
