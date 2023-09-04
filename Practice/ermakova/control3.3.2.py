key = int(input("Введите ключ к цифровому паролю: "))
kod = int(input("Введите контрольный код: "))
parol1 = kod ^ key
print(f"Цифровой пароль равен: {parol1}")
