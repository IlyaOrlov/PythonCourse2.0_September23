def outer_fun(fun):
    def inner_fun(*args, **kwargs):
        # какой-то код, который должен выполняться перед вызовом исходной функции
        res = fun(*args, **kwargs)
        # какой-то код, который должен выполняться после вызова исходной функции
        return res

    return inner_fun