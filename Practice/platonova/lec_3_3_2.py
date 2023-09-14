x = int(input("Введите Ваш секретный код: "))
key = 100
chek = x ^ key
print(f"Ваш цифровой пароль: {chek}")