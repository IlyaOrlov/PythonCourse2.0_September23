def fun1(a, b):
    if a > b:
        print(a)
    else:
        print(b)


def fun2(a, b):
    if a > b:
        return a
    else:
        return b


a = int(input("Введите число: "))
b = int(input("Введите число: "))
print(fun1(a, b))
fun2(a, b)
