import random


a = int(input("Введите первую границу диапазона: "))
b = int(input("Введите вторую границу диапазона: "))
s_num = random.randint(a, b)
while (my_num := input("Введите число: ")).isdecimal():
    my_num = int(my_num)
    if my_num == s_num:
        print(f"Поздравляю, вы угадали число: {s_num}")
        break
    elif my_num > s_num:
        print("Введёное число больше")
    else:
        print("Введёное число меньше")
else:
    print("А тут не число:D")
