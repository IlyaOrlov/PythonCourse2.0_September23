lst = [1, 2, 3]
s = {4, 5, 6}
d = {1:10, 2:20, 3:30}
t = (100, 200, 300)


megalst = [lst, s, d, t]

for obj in megalst:
    print(type(obj))
    for i in obj:  # next()
        print(i)

