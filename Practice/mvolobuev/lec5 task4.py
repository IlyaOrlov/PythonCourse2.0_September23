art = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
for i in range(0, 4):
    print(art[i])

k = int(input("Введите цифру от 1 до 16, столбец которой нужно удалить:   "))
for i in range(0, 4):
    for j in range(0, 4):
        g = art[i]
        if int(g[j]) == k:
            st = j

for i in range(0, 4):
    g = art[i]
    del(g[st])

for i in range(0, 4):
    print(art[i])