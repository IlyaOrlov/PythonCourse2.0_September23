def fun1(a, b):
    print(a if a > b else b)


def fun2(a, b):
    return a if a > b else b


n1 = input("Введите первое число: ")
n2 = input("Введите второе число: ")
fun1(n1, n2)
print(fun2(n1, n2))
