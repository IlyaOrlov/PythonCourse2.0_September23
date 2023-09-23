lst = [[1, 2, 5, 7],
       [3, 2, 2, 1],
       [8, 5, 0, 2]]
number = int(input("Введите число, столбцы с которым надо удалить: "))
ind = set()
for lst1 in lst:
    for j in range(0, len(lst1)):
        if lst1[j] == number:
            ind.add(j)
ind_l = sorted(ind, reverse=True)
for lst1 in lst:
    for x in ind_l:
        del lst1[x]
    print(lst1, sep="\n")
