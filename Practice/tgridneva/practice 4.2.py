temp = input('Введите пятизначное число: ')
result = []
if temp.isdecimal() and len(temp) == 5:
    for i, n in enumerate(temp, 1):
        print(f"{i} == {n}")
else:
    print("Некорректный ввод")
