import time
from random import randint


def list_random(post_list=5):
    return [randint(0, 9) for _ in range(post_list)]


def speed(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        end = time.time()
        print(f"{end - start}\n")
        return res
    return wrapper


@speed
def sort_lst_1(lst):
    print(lst)
    for i, str_lst in enumerate(lst):
        first = lst[i:][0]
        index_min = 0
        min_lst = first
        for index, min_slices in enumerate(lst[i:]):
            if min_slices < min_lst:
                min_lst = min_slices
                index_min = index
        lst[i] = min_lst
        lst[index_min + i] = first
    print(lst)


@speed
def sort_lst_2(lst):
    print(lst)
    for i in range(len(lst) - 1):
        slice_min = i
        for n in range(i + 1, len(lst)):
            if lst[n] < lst[slice_min]:
                slice_min = n
        if i != slice_min:
            lst[i], lst[slice_min] = lst[slice_min], lst[i]
    print(f"{lst}\n")


if __name__ == "__main__":
    sort_lst_1(list_random(20000))
    sort_lst_2(list_random(20000))
