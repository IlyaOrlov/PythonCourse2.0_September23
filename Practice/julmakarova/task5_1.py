def choice_sort(s):
    for i, x in enumerate(arr):
        min_x = min(s[i::])
        if x != min_x:
            i_min = s.index(min_x, i)
            s[i] = min_x
            s[i_min] = x
    return s

arr = [0, 0, 4, 2, 1, 7, 2, 4, 2, 1, 0, 1]
sort_arr = choice_sort(arr)
print(sort_arr)
