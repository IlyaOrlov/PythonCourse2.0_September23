def fun_find_dup(lst):
    for i in range(len(lst) - 1):
        for j in range(i + 1, len(lst)):
            if lst[j] == lst[i]:
                return lst[j]


print(fun_find_dup([1, 2, 4, 3, 2, 1]))