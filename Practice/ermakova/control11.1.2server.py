import socket


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    host = '127.0.0.1'
    port = 12345
    s.bind((host, port))
    s.listen(5)
    dictionary = {'ВМГП': 'Волшебный мир Гарри Поттера',
                  'ЗОТИ': 'Защита от Темных искусств',
                  'ОД': 'Отряд Дамблдора',
                  'УЗМС': 'Уход за магическими существами'}
    while True:
        conn, addr = s.accept()
        with conn:
            print(f'Сервер подключен{addr}')
            shifr = conn.recv(1024)
            words_shifr = shifr.decode().split(',')
            print("Получены зашифрованные слова: ", words_shifr)
            lst_words = []
            for word in words_shifr:
                lst_words.append(dictionary.get(word))
            itog = ','.join(lst_words).encode()
            conn.send(itog)
            print("Отправлена расшифровка!")
