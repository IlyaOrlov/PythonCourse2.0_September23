p = input("Введите пароль: ")
key = 3478
res = int(p) ^ key
print(res)
k = int(input("Введите ключ: "))
if k == key:
    res2 = res ^ key
    print(res2)
else:
    print(f"Неверный ключ")
