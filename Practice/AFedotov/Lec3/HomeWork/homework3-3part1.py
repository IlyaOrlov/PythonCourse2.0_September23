x = int(input("Введите пароль: "))
key = int(input("Введите секретный код: "))
res = x ^ key
print(f"Зашифрованный пароль: {res} \nНе забудьте секретный код!")