find_num = ""
while (num := input("Введите число: ")).lower() != "stop":
    if num.isdecimal():
        find_num += num
    else:
        print("Ошибка! Повтори заново")
print(f"Число сформировано: {find_num}")
