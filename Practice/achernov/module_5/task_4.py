def remove(matrix, digit):
    for line in matrix:
        if digit in line:
            index = line.index(digit)
            for i in range(len(matrix)):
                del matrix[i][index]
    return matrix


my_matrix = [[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]]
new_matrix = remove(my_matrix, 2)
print(my_matrix)
