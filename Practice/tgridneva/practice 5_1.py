def selection_sort(array_to_sort=None):
    if array_to_sort is None:
        array_to_sort = ()
    for i in range(len(array_to_sort)):
        idx_min = i
        for j in range(i + 1, len(array_to_sort)):
            if array_to_sort[j] < array_to_sort[idx_min]:
                idx_min = j
        array_to_sort[idx_min], array_to_sort[i] = array_to_sort[i], array_to_sort[idx_min]
    return array_to_sort


ary = [0, 3, 24, 2, 3, 7]
print(selection_sort(ary))