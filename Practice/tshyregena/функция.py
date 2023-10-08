def fun(*args):
    print(max(args))


def fun_vy(*args):
    return max(args)


a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
fun(a, b)
res = fun_vy(a, b)
print(f"{res}")
