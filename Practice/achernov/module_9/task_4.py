import itertools


def my_iter_merge(arr1, arr2, arr3):
    return list(itertools.chain(arr1 + arr2 + arr3))


def my_iter_len(arr):
    return list(filter(lambda x: len(x) >= 5, arr))


def my_iter_comb(my_pass):
    for i in itertools.combinations(my_pass, 4):
        print(i)


first_task = ([1, 2, 3], [4, 5], [6, 7])
print(my_iter_merge(*first_task))

second_task = (["hello", "i", "write", "cool", "code"])
print(my_iter_len(second_task))

third_task = "password"
my_iter_comb(third_task)



