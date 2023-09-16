b = {'one': 1, 'two': 2, 'three': 3}
b['four'] = 4
print(b)

# k = 'one'
# if k in b:
#     print(b[k])
# else:
#     print(None)

# print(b.get(k))

for key, value in b.items():
    print(f"{key}: {value}")

d = {}
print(type(d))

s = set()
