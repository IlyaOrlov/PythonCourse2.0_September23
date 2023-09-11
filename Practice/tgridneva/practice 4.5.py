from random import randint

number = randint(1, 10)
while 1:
    guess = input("Угадайте целое число от 1 до 10: ")
    if guess == "Выход":
        print("В следующий раз повезёт!")
        break
    guess = int(guess)
    if guess == number:
        print("Вы угадали")
        break
print("Ваше число " + ("больше" if guess > number else "меньше") + ", чем задумал компьютер")
print("Загаданным числом было: " + str(number))
