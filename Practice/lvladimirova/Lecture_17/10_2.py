from multiprocessing import Pool


def add_function(args):
    a, b = args
    if isinstance(a, int) and isinstance(b, int):
        return a + b

    if isinstance(a, str) and isinstance(b, str):
        return f'{a} {b}'

    if isinstance(a, list) and isinstance(b, list):
        return a + b


if __name__ == '__main__':
    my_args = [(1, 2), ("good", "day"), ([1, 2, 3], [4, 5, 6])]
    pool = Pool(processes=4)
    result = pool.map(add_function, my_args)
    print(f"Конечный результат: {result}")
