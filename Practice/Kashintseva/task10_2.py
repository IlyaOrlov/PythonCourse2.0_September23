import multiprocessing


def plus(args):
    a, b = args
    if isinstance(a, int) and isinstance(b, int):
        return a+b
    if isinstance(a, str) and isinstance(b, str):
        return f'{a} {b}'
    if isinstance(a, list) and isinstance(b, list):
        return a + b


if __name__ == '__main__':
    x = [(5, 10), ("Привет,", "мир"), ([1, 2, 3], [10, 20, 30, "всё"])]
    pool = multiprocessing.Pool(processes=3)
    res = pool.map(plus, x)
    print(res)
