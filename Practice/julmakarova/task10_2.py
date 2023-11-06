import multiprocessing


def sum_dif_type(*args):
    try:
        s = args[0]
    except IndexError:
        print("Ошибка в указании аргументов! Не указаны аргументы для сложения.")
        return None

    for a in args[1::]:
        if isinstance(a, type(s)):
            s += a
        else:
            print("Ошибка в указании аргументов! Аргументы должны быть одного типа.")
            return None
    print(s)
    return s


if __name__ == "__main__":
    p_l = (1, 3, "Hello", " world!", [1, 2, 3], [4, 5, 6])
    processes = []

    i = 0
    while i < len(p_l) - 1:
        p = multiprocessing.Process(target=sum_dif_type, args=(p_l[i], p_l[i+1]))
        p.start()
        processes.append(p)
        i += 2

    for p in processes:
        p.join()
