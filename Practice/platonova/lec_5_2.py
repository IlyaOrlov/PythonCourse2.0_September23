def fun_find_dup(lst):
    s = set()
    for i in range(len(lst)):
        if lst[i] in s:
            return lst[i]
        else:
            s.add(lst[i])


print(fun_find_dup([1, 2, 4, 3, 2, 1]))
