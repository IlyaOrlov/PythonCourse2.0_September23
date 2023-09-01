p = input("Введите пароль: ")
key = 3478
res = int(p) ^ key
print(res)
res2 = res ^ key
k = int(input("Введите ключ: "))
if k == key:
    print(res2)
else:
    print(f"Неверный ключ")
