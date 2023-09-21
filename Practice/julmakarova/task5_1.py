def choice_sort(s):
    for i, x in enumerate(s):
        min_x, min_i = min_i_x(s, i)
        if x != min_x:
            s[i], s[min_i] = s[min_i], s[i]

    return s


def min_i_x(s, start=0):
    s = s[start::]
    min_x = s[0]
    min_i = 0
    for i, x in enumerate(s):
        if x < min_x:
            min_x = x
            min_i = i
    min_i += start

    return min_x, min_i


arr = [0, 0, 4, 2, 1, 7, 2, 4, 2, 1, 0, 1]
sort_arr = choice_sort(arr)
print(sort_arr)
