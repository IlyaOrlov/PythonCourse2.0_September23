def fun2(x, y, choose):
    res = choose(x, y)
    print(res)

# Способ 1:
# def fun_max(a, b):
#     return a if a > b else b
#
# def fun_min(a, b):
#     return a if a < b else b
# fun2(10, 20, fun_max)
# fun2(10, 20, fun_min)

# Способ 2:
fun2(10, 20, lambda a, b: a if a > b else b)
fun2(10, 20, lambda a, b: a if a < b else b)
