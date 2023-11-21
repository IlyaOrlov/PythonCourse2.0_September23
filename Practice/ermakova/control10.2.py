import multiprocessing


def summa(*args):
    result = []
    for arg in args:
        if isinstance(arg, int):
            result = sum(args)
        elif isinstance(arg, str):
            result = ''.join(args)
        elif isinstance(arg, list):
            result.extend(arg)
    print(result)


if __name__ == '__main__':
    lst = ((15, 5, 10), ("Привет", " волшебник", "!"), ([1, 2], [3, 4], [5, 6],))
    for i in lst:
        pr = []
        process = multiprocessing.Process(target=summa, args=i)
        process.start()
        pr.append(process)
    for p in pr:
        p.join()
