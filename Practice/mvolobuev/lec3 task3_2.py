cod = input("Введите ваш код :  ")
key = 427
res = int(cod) ^ key
x = int(res) // 10000
y = int(x) * 10000
z = int(res) - int(y)
print(f"Номер вашей ячейки хранения: {x}")
print(f"Пароль вашей ячейки хранения: {z}")
