from random import randint


def matrix_random(post_matrix=5, str_matrix=5):
    return [[randint(0, 9) for _ in range(post_matrix)] for _ in range(str_matrix)]


def matrix_print_beautiful(matrix=[]):
    print("матрица :")
    for str in range(len(matrix)):
        print(matrix[str])


def delete_post_matrix(lst=[], num=7):
    for str in lst:
        while num in str:
            index = str.index(num)
            for dels in lst:
                del dels[index]
    return lst


if __name__ == "__main__":
    lst = matrix_random()
    num = 2
    matrix_print_beautiful(lst)
    lst = delete_post_matrix(lst, num)
    matrix_print_beautiful(lst)
