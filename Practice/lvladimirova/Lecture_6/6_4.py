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


def preobr_matrix(matrix):  # Преобразование матрицы к табличному виду
    for i in matrix:
        for j in i:
            print(j, end=' ')
        print()


arr = [[1, 2, 3, 4, 5], [4, 5, 6, 1, 2], [7, 8, 9, 3, 4]]
print("Исходная матрица: ")
preobr_matrix(arr)
print()
p = int(input("Введите число: "))
new_matrix = fun_matrix(arr, p)
print("Новая матрица: ")
preobr_matrix(new_matrix)
print()
