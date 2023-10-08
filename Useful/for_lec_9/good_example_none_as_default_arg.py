def fun(lst=None):
    if lst is None:
        lst = [1, 2, 3]
    for i in range(len(lst)):
        lst[i] *= lst[i]
    return lst


lst1 = fun([4, 5, 6])
print(lst1)

lst2 = fun()
print(lst2)
