lst = [1, 2, 3, 4, 5]

x = [i ** 2 for i in lst if i < 0]
y = (i ** 2 for i in lst if i < 0)

print(x)
# if len(x) > 0:
#     print(x[0])
# else:
#     print(None)
print(next(iter(x), None))
# print(next(y, 100500))

