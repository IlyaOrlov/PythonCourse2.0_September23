def decor(fun):
    def new_fun(*args, **kwargs):
        print("=============")
        res = fun(*args, **kwargs)
        print("=============")
        return res
    return new_fun


@decor
def fun_sum(a, b):
    res = (a + b)
    print(f"сумма двух чисел: {res}")


fun_sum(10, 5)
