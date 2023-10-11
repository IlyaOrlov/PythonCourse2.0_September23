def fun_dec(fun):
    def fun_nuw(*args):
        print("="*10)
        res = fun(*args)
        print(res)
        print("="*10)

    return fun_nuw


@fun_dec
def fun1(*args):
    return max(args)


a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
fun1(a, b)
