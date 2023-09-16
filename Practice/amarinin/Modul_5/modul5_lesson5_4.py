from random import randint


def matrix_random(post_matrix=5, str_matrix=5):
    return [[randint(0, 9) for _ in range(post_matrix)] for _ in range(str_matrix)]


def matrix_print_beautiful(matrix=None):
    if matrix is None:
        matrix = []
    print("матрица :")
    for str_matrix in range(len(matrix)):
        print(matrix[str_matrix])


def delete_post_matrix(test_lst=None, nums=7):
    for str_lst in test_lst:
        while nums in str_lst:
            index = str_lst.index(nums)
            for dels in test_lst:
                del dels[index]
    return lst


if __name__ == "__main__":
    lst = matrix_random()
    num = 2
    matrix_print_beautiful(lst)
    lst = delete_post_matrix(lst, num)
    matrix_print_beautiful(lst)
