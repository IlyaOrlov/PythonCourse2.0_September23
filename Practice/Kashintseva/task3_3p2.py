x = int(input("Введите шифр: "))
c = int(input("Введите секретный код: "))
x1 = x ^ c
print(f"Расшифрованный пароль: {x1}")