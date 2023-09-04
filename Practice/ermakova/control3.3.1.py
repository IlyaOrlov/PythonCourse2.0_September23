parol = int(input("Введите цифровой пароль: "))
key = int(input("Введите ключ к цифровому паролю: "))
kod = parol ^ key
print(f"Контрольный код равен: {kod}")
