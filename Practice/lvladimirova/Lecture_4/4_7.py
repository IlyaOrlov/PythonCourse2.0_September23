def decor(fun):
    def new_fun(*args, **kwargs):
        print("=============")
        res = fun(*args, **kwargs)
        print("=============")
        return res
    return new_fun


@decor
def fun_perim(a, b):
    res = (a + b) * 2
    print(f"Периметр прямоугольника: {res}")


fun_perim(5, 7)
