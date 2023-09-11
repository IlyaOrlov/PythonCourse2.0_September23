temp = input('Введите пятизначное число: ')
assert len(temp), "Число не пятизначное"
result = []
if temp.isdecimal() and len(temp) == 5:
    for i, n in enumerate(temp, 1):
        print(f"{temp} == {n}")
