ParolAnn = int(input("Введите цифровой пароль: "))
key = 777
encr_password = ParolAnn ^ key
print(f"Зашифрованный пароль пользователя (необходимо запомнить) : {encr_password}")
