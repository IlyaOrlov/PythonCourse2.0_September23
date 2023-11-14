# Написать функцию find_primes(end, start), которая ищет все простые числа в диапазоне от заданного числа start (по умолчанию 3) до заданного числа end. Далее необходимо:
# Запустить ее три раза последовательно в диапазоне от 3 до 10000, от 10001 до 20000, от 20001 до 30000.
#
# Запустить ее три раза с теми же аргументами, но каждый раз в отдельном потоке с помощью threading.Thread. Что будет, если 'забыть' выполнить start или join для потоков?
#
# Запустить ее три раза с теми же аргументами, но каждый раз в отдельном процессе с помощью multiprocessing.Process. Что будет, если 'забыть' выполнить start или join для процессов?
#
# Замерить время исполнения каждого варианта и сравнить результаты.
from math import sqrt
import time
import threading
import multiprocessing

def find_primes(end, start):
    lst = []
    for a in range(start, end + 1):
        for b in range(2, int(sqrt(a) + 1)):
            if a % b == 0: # если остаток от деления = 0, значит не простое
                break
        else:
            lst.append(a)
    print(lst)


if __name__ == '__main__':

    start = time.perf_counter()
    find_primes(10000,3)
    find_primes(20000,10001)
    find_primes(30000,20001)
    print(f'Общее время вычислений в секундах: {time.perf_counter() - start}\n')

    start = time.perf_counter()
    threads = []
    thr1 = threading.Thread(target=find_primes, args=(10000, 1))
    thr2 = threading.Thread(target=find_primes, args=(20000, 10001))
    thr3 = threading.Thread(target=find_primes, args=(30000, 20001))
    thr1.start()
    thr2.start()
    thr3.start()
    thr1.join()
    thr2.join()
    thr3.join()

    print(f'Общее время вычислений в секундах: {time.perf_counter() - start}\n')


    start = time.perf_counter()
    p1 = multiprocessing.Process(target=find_primes, args=(10000, 1))
    p2 = multiprocessing.Process(target=find_primes, args=(20000, 10001))
    p3 = multiprocessing.Process(target=find_primes, args=(30000, 20001))
    p1.start()
    p2.start()
    p3.start()
    p1.join()
    p2.join()
    p3.join()
    print(f'Общее время вычислений в секундах: {time.perf_counter() - start}\n')

# Если без thr.start() (без запуска потока) - поток не запускается. И выходит ошибка: RuntimeError: не удается присоединиться к потоку до его запуска.
# join() явно завершает поток в выбранный момент и освобождает память.
# start() и join() для процессов также.
# Учитывая что задача простая - ее проще реализовывать без потоков и процессов. Затраты на создания потоков оказались больше - время больше, чем без потоков.
# А при создании процессов - времени ушло еще больше, много затратилось ресурсов на создание процессов. Учитывая несложность задачи - это было не целесообразно.
