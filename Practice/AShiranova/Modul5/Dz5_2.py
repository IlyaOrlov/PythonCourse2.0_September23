def first_repeat(s):
    for i, x in enumerate(s):
        if s.index(x, 0, i+1) != i:
            return x


arr = [1, 3, 7, 9, 4, 7, 3, 2]
num = first_repeat(arr)
print(f"Первое повторившееся значение в заданном массиве: {num}")
