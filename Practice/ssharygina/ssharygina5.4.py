def del_st(x, s):
    for n in x:
        i = 0
        while i != len(n):
            if n[i] == s:
                for lst in x:
                    lst.pop(i)
            else:
                i += 1
    return x


x = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16],
    ]
s = int(input("Введите цифру для удаления столбца, который содержит заданную цифру: "))
print(del_st(x, s))
