import socket
import pickle

def send_data(data):
    host = 'mynet'
    port = 13579

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))

        send_data = pickle.dumps(data)
        s.sendall(send_data)

        recv_data = s.recv(1024)

        decoded_data = pickle.loads(recv_data)

        return decoded_data


if __name__ == "__main__":
    encrypted_words = ['par**', 'is***bul', 'Li**on', 'lon**n']
    decrypted_words = send_data(encrypted_words)
    print(decrypted_words)