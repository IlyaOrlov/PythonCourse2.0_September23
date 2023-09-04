password = int(input("Введите цифровой пароль: "))
key = int(input("Введите секретный код: "))
decode_password = password ^ key
print(f"Расшифровка пароля: {decode_password}")