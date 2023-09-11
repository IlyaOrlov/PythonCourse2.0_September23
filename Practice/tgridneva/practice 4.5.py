from random import randint
number = randint(1,10)
quess=int(input("Угадайте целое число от 1 до 10:"))
while quess!=number:
    quess=int(input("Повторите попытку:"))
    if quess<number:
        print("Ваше число меньше, чем задумал компьютер")
    elif quess>number:
        print("Ваше число больше, чем задумал компьютер")
    else:
        print("Вы угадали")
print(quess)
print(number)
