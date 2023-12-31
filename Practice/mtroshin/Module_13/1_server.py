# Написать клиентское и серверное приложения.
# Клиент отправляет на сервер список зашифрованных слов,
# сервер дешифрует слова по словарю и возвращает клиенту список расшифрованных слов.
# Клиент должен вывести полученный список.
import socket

# 1-й параметр - семейство адресов, с которыми будет работать сокет
# AF_INET соответствует адресам IPv4
# 2-й параметр - протокол транспортного уровня
# SOCK_STREAM соответствует протоколу TCP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    host = '127.0.0.1' # '127.0.0.1' соответствует хосту, на котором запускается скрипт
    port = 12345
    s.bind((host, port))
    s.listen(2) # Открываем порт на сервере (не более 2 клиентов одновременно)
    while True:
        conn, addr = s.accept()
        with conn:
            print('Server got connection from {}'.format(addr))
            # Преобразуем строку в набор байтов (ascii в utf-8) и отправляем
            conn.send('Thank you for the connection'.encode())
            f = conn.recv(1024)
            text = f.decode()
            print(f"Зашифрованная строка: {text}")

            dict_code = {'В':'Россия', 'траве':'одержит','сидел':'победу','кузнечик':'в священной битве','зелененький':'гегемония США и саттелитов',' он':' будет','был':'повержена'}

            for item in dict_code:
                text = text.replace(item, dict_code[item])

            print(f"Расшифрованная строка: {text}")
            conn.send(text.encode())
