def funsr(a, b):
    if a > b:
        print(a)
    else:
        print(b)


def fun2(a, b):
    if a > b:
        return a
    else:
        return b


a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
print(funsr(a, b))
print(fun2(a, b))
