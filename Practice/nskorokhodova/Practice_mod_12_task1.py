import math
import time
import threading
import multiprocessing


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


def find_primes(end, start=3):
    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    return primes


if __name__ == '__main__':
    t1 = threading.Thread(target=find_primes, args=(10000,))
    t2 = threading.Thread(target=find_primes, args=(20000, 10001,))
    t3 = threading.Thread(target=find_primes, args=(30000, 20001,))

    start_time = time.time()
    t1.start()
    t2.start()
    t3.start()
    print("Потоки запущены")

    start = time.perf_counter()
    threads = []
    for args in ((10000, 3), (20000, 10001), (30000, 20001)):
        thr = threading.Thread(target=find_primes, args=args)
        thr.start()
        threads.append(thr)
    for j in threads:
        j.join()

    print(f'Общее время вычислений потоков в секундах: {time.perf_counter() - start}\n')

    p1 = multiprocessing.Process(target=find_primes, args=(10000,))
    p2 = multiprocessing.Process(target=find_primes, args=(20000, 10001,))
    p3 = multiprocessing.Process(target=find_primes, args=(30000, 20001,))

    start_time = time.time()
    p1.start()
    p2.start()
    p3.start()
    print("Процессы запущены")

    start = time.perf_counter()
    proc = []
    for args_proc in ((10000, 3), (20000, 10001), (30000, 20001)):
        p = multiprocessing.Process(target=find_primes, args=args_proc)
        p.start()
        proc.append(p)
    for pr in proc:
        pr.join()

    print(f'Общее время вычислений процессов в секундах: {time.perf_counter() - start}\n')
