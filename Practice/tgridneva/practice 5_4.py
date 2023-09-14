def remove_column(list, digit):
    for row in list:
        if digit in row:
            row.remove(digit)
    return list


matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

new_matrix = remove_column(matrix, 2)
print(new_matrix)
