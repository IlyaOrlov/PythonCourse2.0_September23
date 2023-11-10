import socket


sh = {"Мск": "Москва", "НН": "Нижний Новгород", "Гусь": "Гусь-Хрустальный", "СПБ": "Санкт-Петербург"}
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    host = '127.0.0.1'
    port = 12345
    s.bind((host, port))
    s.listen(5)
    while True:
        conn, addr = s.accept()
        with conn:
            print(f"Подключение установилось c адреса {addr}. Ждем список слов.")
            c = conn.recv(1024).decode().split(",")
            c1 = ""
            for i in c:
                if i in sh:
                    c1 += sh[i] + " "
            conn.send(c1.encode())
            print(f"Список расшифрованных слов направлен.")
