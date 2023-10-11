def fun(lst):
    for element in lst:
        if lst.count(element) > 1:
            return element


lst1 = [6, 78, 8, 25, 8, 5]
print(fun(lst1))
