def fun1(a, b):
    print(a if a > b else b)


def fun2(a, b):
    return a if a > b else b


x = input("Введите первое число: ")
y = input("Введите второе число: ")
fun1(x, y)
print(fun2(x, y))
