def fun_dec(fun):
    def fun_nuw(*args):
        print("="*10)
        print(max(args))
        print("="*10)

    return fun_nuw


@fun_dec
def fun(*args):
    print(max(args))


a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
fun(a, b)
