import socket


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    host = '127.0.0.1'
    port = 12345
    s.connect((host, port))
    words = ["Мск", "СПБ", "НН", "Гусь", "Новосиб"]
    s.send(",".join(words).encode())
    print(f"Список зашифрованных слов направлен")
    d = s.recv(1024)
    print(d.decode())
