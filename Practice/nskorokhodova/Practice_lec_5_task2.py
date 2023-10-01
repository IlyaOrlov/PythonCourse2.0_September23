def repeat(s):
    for i, n in enumerate(s):
        if s.index(n) != i:
            return n
    print("Нет повторений!")


ar = [2, 3, 4, 5, 3, 2]
res = repeat(ar)
print(res)
