def decor(fun):
    def new_fun(*args, **kwargs):
        print("=============")
        res = fun(*args, **kwargs)
        print("=============")
        return res
    return new_fun


@decor
def text(a, b):
    print(a + b)


text(5, 7)