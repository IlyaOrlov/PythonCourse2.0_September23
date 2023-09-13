import time


def calc_time(fun):
    def new_fun(*args, **kwargs):
        start = time.time()
        res = fun(*args, **kwargs)
        finish = time.time()
        print(f"Затрачено времени: {finish - start}")
        return res

    return new_fun


def hello_bye_dec(fun):
    def new_fun(*args, **kwargs):
        print("Hello")
        res = fun(*args, **kwargs)
        print("Bye!")
        return res

    return new_fun


@calc_time
@hello_bye_dec
def fun_sum(x, y):
    res = x + y
    return res


@calc_time
def fun_mul(x, y):
    res = x * y
    return res


@calc_time
def fun_sqr(x):
    res = x * x
    return res


res = fun_sum(10, 20)
print(res)
