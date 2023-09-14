arg = [0, 3, 24, 2, 3, 7]
print(arg)
for i in range(0, len(arg)-1):
    for k in range(i+1, len(arg)):
        if int(arg[k]) < int(arg[i]):
            arg[i], arg[k] = arg[k], arg[i]
print(arg)