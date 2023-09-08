fin_num = ""
while (num := input("Введите число: ")).lower() != "stop":
    if num.isdecimal():
        fin_num += num
    else:
        print("Введено некорректное значение, введите пожалуйста число!")
print(f"Итоговое число равно: {fin_num}")
