def primer_outer (fun):
    def primer_inner (*args,**kwargs):
        print("===========")
        res = fun(*args,**kwargs)
        print(res)
        print("===========")
        return res
    return primer_inner


def fun(x, y):
    return x + y


fun = primer_outer(fun)
fun(10,5)
