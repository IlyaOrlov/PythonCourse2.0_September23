
def display(matrix1):
    for r in matrix1:
        print(r)


matrix = [[5, 4, 3],
          [6, 6, 7],
          [3, 9, 0]]
row1 = [matrix[0][0], matrix[1][0], matrix[2][0]]
row2 = [matrix[0][1], matrix[1][1], matrix[2][1]]
row3 = [matrix[0][2], matrix[1][2], matrix[2][2]]
p = int(input("Какое число вы хотите удалить: "))
if p in row1:
    del [matrix[0][0], matrix[1][0], matrix[2][0]]
if p in row2:
    del [matrix[0][1], matrix[1][1], matrix[2][1]]
if p in row3:
    del [matrix[0][2], matrix[1][2], matrix[2][2]]
matrix1 = matrix
print(display(matrix1))
