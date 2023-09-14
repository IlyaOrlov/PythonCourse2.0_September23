def line_fun(fun):
    def new_fun(*args, **kwargs):
        print("===========")
        res = fun(*args, **kwargs)
        print("===========")
        return res
    return new_fun


@line_fun
def fun_str(x, y):
    sum_str = x + y
    print(sum_str)


x1 = "Привет "
y1 = "волшебник!!!"
fun_str(x1, y1)
