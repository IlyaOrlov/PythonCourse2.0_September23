# lst = [1, 2, 3]
#
# it = iter(lst)
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))

s = {1: "a", 2:"b", 3:"c"}

it = iter(s)
while True:
    try:
        print(next(it))
    except StopIteration:
        break

for x in s:
    print(x)

# x = True
# while True:
#     print("Hello")

# i = 0
# while i < len(lst):
#     print(lst[i])
#     i += 1

