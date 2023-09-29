x = ""
y = ""
while (x := input("Введите число: ")).lower() != "stop":
    if x.isdecimal():
        y += x
    else:
        print("Ошибка! Вы ввели не число")
print(f"Получилось число: {y}")