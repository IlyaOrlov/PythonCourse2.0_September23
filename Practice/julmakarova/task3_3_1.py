user_password = int(input("Введите цифровой пароль: "))
key = 12345
encr_password = user_password ^ key
print(f"Зашифрованный пароль пользователя (необходимо запомнить) : {encr_password}")
