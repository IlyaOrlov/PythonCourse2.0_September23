def dec_fun(fun):
    def fun1(*args, **kwargs):
        print("============================")
        res = fun(*args, **kwargs)
        print("============================")
        return res

    return fun1


@dec_fun
def perim(dlina, shir):
    per = (dlina + shir) * 2
    print(f"Периметр прямоугольника = {per}")


perim(5, 20)
