def ud(x, y):
    for n in x:
        i = 0
        while i != len(n):
            if n[i] == y:
                for lst in x:
                    lst.pop(i)
            else:
                i += 1
    return x


x = [
    [1, 3, 5, 7],
    [1, 4, 1, 4],
    [5, 8, 5, 8],
    ]
y = int(input("Введите цифру к удалению : "))
x1 = ud(x, y)
print(x1)
