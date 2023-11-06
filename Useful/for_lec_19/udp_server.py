import socket

# AF_INET соотвествует адресам IPv4
# SOCK_DGRAM соотвествует протоколу UDP
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    host = '127.0.0.1'
    port = 12345
    s.bind((host, port))
    while True:
        data, addr = s.recvfrom(1024)
        print(f'Server got data from client: {data.decode()}')
        s.sendto('Thank you for the data'.encode(), addr)
