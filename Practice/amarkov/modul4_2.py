a = input("Введите число: ")
numbers = []

for char in a:
     print(char)

i = 1 # ввели переменную от которой начать счёт
for char in a:
     print(f"{i} цифра равна {char}")