import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 12345
s.connect((host, port))  # подключаемся к серверу
d = s.recv(1024)  # получаем данные от сервера (1024 байта - размер буфера для данных)
# преобразуем данные из байтового представления в строковое и выводим
# (преобразование из utf-8 в ascii)
print(d.decode())
s.send("В траве сидел кузнечик, зелененький он был!".encode())
d2 = s.recv(1024)
print(f"Расшифровка: {d2.decode()}")
s.close()

