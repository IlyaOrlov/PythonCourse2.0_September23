lst = [5, 78, 4, 34]
for k in range(len(lst)):
    nM = k
    for i in range(k, len(lst)):
        if lst[i] < lst[nM]:
            nM = i
    lst[k], lst[nM] = lst[nM], lst[k]
print(lst)
