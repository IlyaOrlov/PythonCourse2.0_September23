def fun(lst):
    res = set()
    for element in lst:
        if element in res:
            return element
        else:
            res.add(element)


lst1 = [4, 9, 8, 9, 1, 8, 6]
print(fun(lst1))
