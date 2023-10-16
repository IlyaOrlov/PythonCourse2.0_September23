def fun_dec(fun):
    def fun_nuw(*args, **kwargs):
        print("="*10)
        res = fun(*args, **kwargs)
        print(res)
        print("="*10)
        return res
    return fun_nuw


@fun_dec
def fun1(*args):
    return max(args)


a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
fun1(a, b)
