d = {}
while (s := input("Введите слово: ")) != "stop":
    if s in d:
        d[s] += 1
    else:
        d[s] = 1

print(d)
