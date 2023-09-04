x = int(input("Введите число: "))
y = int(input("Введите число: "))
res = x if x >= y else y
print(res)

if x > y:
    res = x
else:
    res = y
print(res)
