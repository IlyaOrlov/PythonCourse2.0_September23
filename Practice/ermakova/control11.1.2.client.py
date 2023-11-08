import socket


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    host = '127.0.0.1'
    port = 12345
    s.connect((host, port))
    client_words_shifr = ['ВМГП', 'ЗОТИ', 'ОД', 'УЗМС']
    s.send(','.join(client_words_shifr).encode())
    print("Отправлен список зашифрованных слов:", client_words_shifr)
    deshifr = s.recv(1024).decode()
    itog_deshifr = deshifr.split(',')
    print("Получен список расшифрованных слов:", itog_deshifr)
