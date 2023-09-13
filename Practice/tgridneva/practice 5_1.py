def selection_sort(array_to_sort=None):
    a = array_to_sort
    for i in range(len(a)):
        idx_min = i
        for j in range(i + 1, len(a)):
            if a[j] < a[idx_min]:
                idx_min = j
        tmp = a[idx_min]
        a[idx_min] = a[i]
        a[i] = tmp
    return a


ary = [0, 3, 24, 2, 3, 7]
print(selection_sort(ary))
