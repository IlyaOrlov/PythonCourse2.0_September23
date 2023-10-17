def fun_max1(a, b):
    if a > b:
        print(a)
    else:
        print(b)


def fun_max2(a, b):
    if a > b:
        return a
    else:
        return b


x1 = int(input("Введите первое число: "))
x2 = int(input("Введите второе число: "))
fun_max1(x1, x2)
print(fun_max2(x1, x2))
