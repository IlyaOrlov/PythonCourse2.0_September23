from random import randint


def fun_reply(lst):
    x = None
    for i, id_x in enumerate(lst):
        if lst.index(id_x, 0, i + 1) != i:
            x = lst[i]
            break
    if x is None:
        return "Повторяюшихся символов нет!"
    else:
        return f"Первый повторившийся символ {x}"


lst_new = [randint(1, 40) for _ in range(15)]
print(lst_new)
print(fun_reply(lst_new))
