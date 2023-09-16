def del_column(s, flag):
    for x in s:
        i = 0
        while i != len(x):
            if x[i] == flag:
                for lst in s:
                    lst.pop(i)
            else:
                i += 1
    return s


arr = [[1, 0, 0, 0, 1], [2, 4, 0, 4, 2], [0, 2, 1, 0, 0]]
num = int(input("Введите число: "))
new_arr = del_column(arr, num)
print(f"Матрица с удаленными столбцами: {new_arr}")
