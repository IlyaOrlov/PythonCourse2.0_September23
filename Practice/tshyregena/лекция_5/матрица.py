
def display(matrix1):
    for r in matrix1:
        print(r)


def display2(matrix3):
    new_mat = []
    for k in range(len(matrix3[0])):
        new_row = []
        for el in matrix3:
            new_row.append(el[k])
        new_mat.append(new_row)
    return new_mat


matrix2 = [[5, 4, 3, 8],
           [6, 6, 7, 8],
           [3, 9, 0, 6]]
display(matrix2)
new_mat1 = display2(matrix2)
p1 = int(input("Столбец с каким числом вы хотите удалить: "))
i = 0
while i < len(new_mat1):
    if p1 in new_mat1[i]:
        del new_mat1[i]
    else:
        i += 1
new_mat2 = display2(new_mat1)
display(new_mat2)
