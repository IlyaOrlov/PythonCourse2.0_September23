art = [[1, 2, 3, 4], [5, 6, 2, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
st = [-1, -1, -1, -1]
for i in range(0, 4):
    print(art[i])

k = int(input("Введите цифру от 1 до 16, столбец которой нужно удалить:   "))
i1 = 0
for i in range(0, 4):
    for j in range(0, 4):
        g = art[i]
        if int(g[j]) == k:
            st[i1] = j
            i1 += 1
print(st)
for j1 in range(0, i1):
    s1 = st[j1]
    for i in range(0, 4):
        g = art[i]
        del (g[s1])

for i in range(0, 4):
    print(art[i])