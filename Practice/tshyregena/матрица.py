
def display(matrix1):
    for r in matrix1:
        print(r)


def display2(matrix3):
    new_mat = []
    for k in range(len(matrix3[0])):
        new_row = []
        for el in matrix3:
            new_row.append(el[i])
        new_mat.append(new_row)
    return new_mat


# matrix = [[5, 4, 3],
#           [6, 6, 7],
#           [3, 9, 0]]
# row1 = [matrix[0][0], matrix[1][0], matrix[2][0]]
# row2 = [matrix[0][1], matrix[1][1], matrix[2][1]]
# row3 = [matrix[0][2], matrix[1][2], matrix[2][2]]
# p = int(input("Какое число вы хотите удалить: "))
# if p in row1:
#     del [matrix[0][0], matrix[1][0], matrix[2][0]]
# if p in row2:
#     del [matrix[0][1], matrix[1][1], matrix[2][1]]
# if p in row3:
#     del [matrix[0][2], matrix[1][2], matrix[2][2]]
# matrix1 = matrix
# display(matrix1)
matrix2 = [[5, 4, 3, 8],
           [6, 6, 7, 8],
           [3, 9, 0, 6]]
new_mat = display2(matrix2)
print(new_mat)
p1 = int(input("Какое число вы хотите удалить: "))
i = 0
while i < len(new_mat):
    if p1 in new_mat[i]:
        del new_mat[i]
    else:
        i += 1
display(new_mat)
