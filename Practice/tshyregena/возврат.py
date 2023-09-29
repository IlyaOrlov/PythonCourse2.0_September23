def fun(lst):
    res = []
    for element in lst:
        while lst.count(element) > 1 and element not in res:
            if len(res) == 0:
                res.append(element)
            else:
                break
    return res


lst = [5, 78, 8, 25, 8, 5]
print(fun(lst))
