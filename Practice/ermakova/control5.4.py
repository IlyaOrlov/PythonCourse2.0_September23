lst = [[1, 2, 5, 7],
       [3, 4, 2, 1],
       [8, 5, 0, 2]]

number = int(input("Введите число, столбцы с которым надо удалить: "))
ind = []
for i in range(0, len(lst)):
    for j in range(0, len(lst[i])):
        if lst[i][j] == number:
            ind.append(j)
ind.sort()
for i in range(0, len(lst)):
    for x in reversed(range(0, len(ind))):
        del lst[i][ind[x]]
    print(lst[i], sep="\n")
