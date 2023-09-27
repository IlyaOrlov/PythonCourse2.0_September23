arg = [0, 3, 24, 2, 3, 7]
print(arg)
for i in range(0, len(arg)-1):
    n = i
    for k in range(i + 1, len(arg)):
        if arg[k] < arg[n]:
            n = k
    arg[i], arg[n] = arg[n], arg[i]
print(arg)
