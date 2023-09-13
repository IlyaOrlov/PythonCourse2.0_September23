from random import randint


lst = [randint(1, 40) for _ in range(10)]
print(lst)
x = []


def fun_reply():
    for i in range(len(lst)):
        for n in range(i+1, len(lst)):
            if lst[i] == lst[n]:
                x.append(lst[n])
                break
    if x == []:
        print("Повторяющихся символов нет!")
    else:
        print(f"Первый повторяющийся символ {x[0]}")


fun_reply()
