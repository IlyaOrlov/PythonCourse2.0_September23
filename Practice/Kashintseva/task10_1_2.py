from threading import Thread
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
pr1 = Thread(target=find_primes, args=(3, 10000))
pr2 = Thread(target=find_primes, args=(10001, 20000))
pr3 = Thread(target=find_primes, args=(20001, 30000))
pr1.start()
pr2.start()
pr3.start()
pr1.join()
pr2.join()
pr3.join()
print(f'Затрачено на выполнение {time.perf_counter() - st:.2f} sec.')
# Время выполнения 69.13 секунд
# Если 'забыть' выполнить start для потоков, то потоки не начнут выполнять свои операции.
# Если 'забыть' выполнить join для потоков, то главный поток не будет ждать окончания выполнения операции
# определенного потока, а во время его работы может добавить результат другого потока.
