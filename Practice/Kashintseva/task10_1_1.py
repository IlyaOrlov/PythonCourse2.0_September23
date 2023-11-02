import time


def find_primes(start=3, end=None):
    if end is None:
        end = start
    lst = []
    for i in range(start, end+1):
        d = 0
        for x in range(2, i):
            if i % x == 0:
                d += 1
        if d < 1:
            lst.append(i)
    return lst


st = time.perf_counter()
pr1 = find_primes(3, 10000)
pr2 = find_primes(10001, 20000)
find_primes(20001, 30000)
print(f'Затрачено на выполнение {time.perf_counter() - st:.2f} sec.')
#Время выполнения 65.37 секунд
