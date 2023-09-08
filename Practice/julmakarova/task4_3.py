num = input("Введите число: ")
fin_num = ""
while num != "Stop" and num != "stop" and num != "STOP":
    if num.isdecimal():
        fin_num += num
    else:
        print("Введено некорректное значение, введите пожалуйста число!")
    num = input()
print(f"Итоговое число равно: {fin_num}")

