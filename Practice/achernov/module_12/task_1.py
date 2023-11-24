import multiprocessing
from threading import Thread
import time


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def find_primes(end, start):
    primes = []
    for num in range(start, end - 1):
        if is_prime(num):
            primes.append(num)
    return primes


if __name__ == "__main__":
    star_time = time.time()
    res1 = find_primes(10000, 3)
    res2 = find_primes(20000, 10001)
    res3 = find_primes(30000, 20001)
    end_time = time.time()
    timer = end_time - star_time
    print(f"Затрачено времени на поэтапный запууск: {timer} сек")

    start_time = time.perf_counter()
    t1 = Thread(target=find_primes, args=(10000, 3))
    t2 = Thread(target=find_primes, args=(20000, 10001))
    t3 = Thread(target=find_primes, args=(30000, 20001))
    t1.start()
    t2.start()
    t3.start()
    t1.join()
    t2.join()
    t3.join()
    print(f"Время выполнения в потоках {time.perf_counter() - start_time} сек")

    start_time = time.perf_counter()
    p1 = multiprocessing.Process(target=find_primes, args=(3, 10000))
    p2 = multiprocessing.Process(target=find_primes, args=(10001, 20000))
    p3 = multiprocessing.Process(target=find_primes, args=(20001, 30000))
    p1.start()
    p2.start()
    p3.start()
    p1.join()
    p2.join()
    p3.join()
    print(f"Время выполнения в разных процессах {time.perf_counter() - start_time} сек")

# Если не выполнить start() в потоках и процессах, то они не будут запущены
# Если не выполнить join() в потоках и процессах, то программа не будет дожидаться завершения всех дочерних потоков
# и процессов
# Распараллеливание по потокам не дает преимущества во времени в задачах CPU- bound (происходит это по причине
# GIL - глобальной блокировки интерпретатора (каждый из потоков полностью "захватывает" процессор для своего выполнения)
# Распараллеливание по процессам не дало преимуществ в данной задаче, поскольку расходы на создание процессов
# не окупились, объемы вычислений не достаточно велики для вычисления в разных процессах
