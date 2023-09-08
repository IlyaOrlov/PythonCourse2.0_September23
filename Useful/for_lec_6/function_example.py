import random


def input_int(prompt: str) -> int:
    while not (i := input(prompt)).isdecimal():
        print("Ошибка! Вы ввели НЕ число!")
    i = int(i)
    return i


start = input_int("Введите начало диапазона: ")
end = input_int("Введите конец диапазона: ")
print(random.randint(start, end))
