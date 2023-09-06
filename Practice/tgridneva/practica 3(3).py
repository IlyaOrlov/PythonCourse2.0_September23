password = int(input("Введите цифровой пароль: "))
key = int(input("Введите секретный код: "))
encode_password = password ^ key
print(f"Шифрование пароля: {encode_password}")
