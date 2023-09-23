def fun_matrix(matrix, element):
    for x in matrix:
        y = 0
        while y != len(x):
            if x[y] == element:
                for lst in matrix:
                    lst.pop(y)
            else:
                y += 1
    return matrix


def fun_zamena(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end=' ')
        print()


arr = [[1, 2, 3, 4, 5], [4, 5, 6, 1, 2], [7, 8, 9, 3, 4]]
print("Исходная матрица: ")
fun_zamena(arr)
print()
p = int(input("Введите число: "))
new_matrix = fun_matrix(arr, p)
print("Новая матрица: ")
fun_zamena(new_matrix)
print()
