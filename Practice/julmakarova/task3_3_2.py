encr_password = int(input("Введите зашифрованный пароль: "))
key = 12345
user_password = encr_password ^ key
print(f"Цифровой пароль пользователя: {user_password}")
