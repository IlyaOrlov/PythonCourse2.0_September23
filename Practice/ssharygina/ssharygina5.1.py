def sort(s):
    for i, x in enumerate(s):
        min_x, min_i = min1(s, i)
        if x != min_x:
            s[i], s[min_i] = s[min_i], s[i]
    return s


def min1(s, start=0):
    s = s[start::]
    min_x = s[0]
    min_i = 0
    for i, x in enumerate(s):
        if x < min_x:
            min_x = x
            min_i = i
    min_i += start
    return min_x, min_i


s1 = [7, 5, 8, 21, 50, 1, 2, 9, 2, 15, 0, -1]
print(f"Отсортированный список: {sort(s1)}")
