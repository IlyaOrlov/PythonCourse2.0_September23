import math

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

import time

# Последовательное выполнение
start_time = time.time()
primes1 = find_primes(10000)
print(f"Время выполнения первого диапазона: {time.time() - start_time} сек")

start_time = time.time()
primes2 = find_primes(20000, 10001)
print(f"Время выполнения второго диапазона: {time.time() - start_time} сек")

start_time = time.time()
primes3 = find_primes(30000, 20001)
print(f"Время выполнения третьего диапазона: {time.time() - start_time} сек")

import threading

t1 = threading.Thread(target=find_primes, args=(10000,))
t2 = threading.Thread(target=find_primes, args=(20000, 10001,))
t3 = threading.Thread(target=find_primes, args=(30000, 20001,))

start_time = time.time()
t1.start()
t2.start()
t3.start()
print("Потоки запущены")

# Если 'забыть' выполнить start или join для потоков, они так и останутся в состоянии запуска
# и не приведут к результату. В этом случае программа может зависнуть, так как главный поток
# не будет дожидаться завершения дочерних потоков и может завершиться раньше их завершения.

import multiprocessing

# Многопроцессное выполнение
p1 = multiprocessing.Process(target=find_primes, args=(10000,))
p2 = multiprocessing.Process(target=find_primes, args=(20000, 10001,))
p3 = multiprocessing.Process(target=find_primes, args=(30000, 20001,))

start_time = time.time()
p1.start()
p2.start()
p3.start()
print("Процессы запущены")

# Если 'забыть' выполнить start или join для процессов, они так и останутся в состоянии запуска
# и не приведут к результату. Однако, в отличие от потоков, процессы работают независимо друг от
# друга, поэтому главный процесс может продолжить выполняться и завершиться, не дожидаясь завершения
# дочерних процессов. В этом случае дочерние процессы будут продолжать работать независимо до
# своего завершения.

start_time = time.time()
# Выполнение функции или запуск потоков/процессов
print(f"Время выполнения: {time.time() - start_time} сек")