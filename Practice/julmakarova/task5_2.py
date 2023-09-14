def first_repeat(s):
    for i, x in enumerate(s):
        if x in s[:i:]:
            return x


arr = [2, 3, 4, 2, 4, 6, 3, 2]
num = first_repeat(arr)
print(f"Первое повторившееся значение в заданном массиве: {num}")
