password = int(input("Придумайте пароль: "))
key = int(input("Придумайте ключ: "))
res = password ^ key
print(f"Ваш секретный код: {res}")
