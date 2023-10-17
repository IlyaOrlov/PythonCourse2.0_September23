def my_enumerate(lst):
    i = 0
    while i < len(lst):
        res = i, lst[i]
        i += 1
        yield res


lst1 = ["a", "b", "c", "d"]
m = my_enumerate(lst1)

for i, x in my_enumerate(lst1):
    print(i, x)

print("=====================")

for i, x in my_enumerate(lst1):
    print(i, x)