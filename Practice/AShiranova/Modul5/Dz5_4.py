def ud(m, c):
    for n in m:
        i = 0
        while i != len(n):
            if n[i] == c:
                for lst in m:
                    lst.pop(i)
            else:
                i += 1
    return m


m = [
    [1, 2, 3, 5],
    [1, 4, 1, 5],
    [2, 3, 1, 4],
    ]
c = int(input("Напишите цифру, которую нужно удалить: "))
m1 = ud(m, c)
print(m1)
