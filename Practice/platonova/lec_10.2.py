import multiprocessing


def sum_dif_type(*args):
    try:
        x = args[0]
    except IndexError:
        return None

    for a in args[1::]:
        if isinstance(a, type(x)):
            x += a
        else:
            return None
    print(x)
    return x


if __name__ == "__main__":
    p_l = (2, 10, "Текст", " Текст2", [1, 2, 3], [4, 5, 6])
    processes = []

    i = 0
    while i < len(p_l) - 1:
        p = multiprocessing.Process(target=sum_dif_type, args=(p_l[i], p_l[i+1]))
        p.start()
        processes.append(p)
        i += 2

    for p in processes:
        p.join()