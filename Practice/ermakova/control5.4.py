lst = [[1, 2, 5, 7],
       [3, 2, 2, 1],
       [8, 5, 0, 2]]
number = int(input("Введите число, столбцы с которым надо удалить: "))
ind = []
for i in range(0, len(lst)):
    for j in range(0, len(lst[i])):
        if lst[i][j] == number:
            if j in ind:
                j += 1
            else:
                ind.append(j)
ind.sort(reverse=True)
for i in range(0, len(lst)):
    for x in ind:
        del lst[i][x]
    print(lst[i], sep="\n")
