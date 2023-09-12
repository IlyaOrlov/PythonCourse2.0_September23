p = int(input("Введите пароль: "))
c = int(input("Введите секретный код: "))
x = p ^ c
print(f"Шифр: {x}")
