from random import randint

number = randint(1, 10)
while (quess := input("Угадайте целое число от 1 до 10:")).isdecimal():
    quess = int(quess)
    if quess < number:
        print("Ваше число меньше, чем задумал компьютер")
    elif quess > number:
        print("Ваше число больше, чем задумал компьютер")
    else:
        print("Вы угадали")
        break
print(quess)
print(number)
