def remove(matrix, digit):
    for x in matrix:
        i = 0
        while i != len(x):
            if x[i] == digit:
                for lst in matrix:
                    lst.pop(i)
            else:
                i += 1
    return matrix


test = [[1, 2, 3],
        [1, 2, 3],
        [1, 2, 3]]
new_matrix = remove(test, int(input("Введите число: ")))
print(new_matrix)
