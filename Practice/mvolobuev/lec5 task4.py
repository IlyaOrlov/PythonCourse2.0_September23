art = [[1, 2, 3, 4], [5, 2, 2, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
st = [-1, -1, -1, -1]
for i in range(0, 4):
    print(art[i])

k = int(input("Введите цифру от 1 до 16, столбец которой нужно удалить:   "))
i1 = 0
for i in range(0, len(art)):
    for j in range(0, len(art[0])):
        g = art[i]
        if g[j] == k:
            st[i1] = j
            if st[i1] == st[i1-1]:
                st[i1] = -1
            else:
                i1 +=1

for j1 in range(0, i1):
    s1 = st[j1]
    for i in range(0, len(art)):
        g = art[i]
        del(g[s1-j1])
for i in range(0, len(art) - 1):
    print(art[i])
