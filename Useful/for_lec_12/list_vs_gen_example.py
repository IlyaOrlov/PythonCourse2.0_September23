a = [x for x in range(10)]
print(a)

b = (x for x in range(10))
print(b)
for n in b:
    print(n)