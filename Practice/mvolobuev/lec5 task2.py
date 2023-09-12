def fun_povtor(st):
    j1 = len(st)
    j2 = len(st)
    for i in range(0, len(st) - 1):
        for k in range(i + 1, len(st)):
            if int(st[k]) == int(st[i]):
                if k-i < j2:
                    j1 = st[k]
                    j2 = k-i
    print(f"Первый повторившийся символ: {j1}")




arg = [2, 3, 4, 5, 3, 2]
print(arg)
fun_povtor(arg)
