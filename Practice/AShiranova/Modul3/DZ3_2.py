encr_password = int(input("Введите зашифрованный пароль: "))
key = 777
ParolAnn = encr_password ^ key
print(f"Цифровой пароль пользователя: {ParolAnn}")
