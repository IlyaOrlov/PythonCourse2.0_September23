from random import randint


def list_random(post_list=5):
    return [randint(0, 9) for _ in range(post_list)]


if __name__ == "__main__":
    lst = list_random(20)
    print(lst)
    for i, str in enumerate(lst):
        lst_i = lst[i:]
        first = lst_i[0]
        index_min = 0
        min_lst = first
        for index, min in enumerate(lst_i):
            if min < min_lst:
                min_lst = min
                index_min = index
        lst[i] = min_lst
        lst[index_min + i] = first
    print(lst)
