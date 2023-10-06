def remove(matrix, digit):
    for line in matrix:
        i = 0
        while i != len(line):
            if line[i] == digit:
                for lst in matrix:
                    lst.pop(i)
            else:
                i += 1
    return matrix


my_matrix = [[1, 2, 2],
             [4, 5, 6],
             [7, 8, 9]]
new_matrix = remove(my_matrix, int(input("Введите число: ")))
print(new_matrix)
