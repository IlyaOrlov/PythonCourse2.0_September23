ch1 = ""
while (ch := input("Введите число: ")).lower() != "stop":
    if ch.isdecimal():
        ch1 += ch
    else:
        print("Введено не число! Повторите ввод:")
print(f"Число из введенных символов равно: {ch1}")
