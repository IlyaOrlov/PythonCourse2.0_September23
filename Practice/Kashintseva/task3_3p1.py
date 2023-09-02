pas = int(input("Введите пароль: "))
c = int(input("Введите секретный код: "))
x = pas ^ c
print(f"Шифр: {x}")
