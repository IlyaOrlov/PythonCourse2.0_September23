def fun(lst):
    res = []
    for element in lst:
        if element in res:
            return element
        else:
            res.append(element)


lst1 = [3, 9, 8, 3, 1, 8, 6]
print(fun(lst1))
