res = int(input("Введите свой секретный код: "))
key = int(input("Введите свой секретный ключ: "))
res_2 = res ^ key
print(f"Расшифровка готова: {res_2}")