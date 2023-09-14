def remove_column(spisok, digit):
    for row in spisok:
        del row[digit]
    return spisok


matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

new_matrix = remove_column(matrix, 2)
print(new_matrix)
