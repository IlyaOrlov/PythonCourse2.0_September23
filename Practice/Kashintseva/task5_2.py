def repeat(*args):
    for i, n in enumerate(s):
        if s.count(n) > 1:
            return n


s = [3, 8, 5, 6, 5, 9, 6, 5]
res = repeat(s)
print(res)
