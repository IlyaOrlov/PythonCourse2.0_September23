import time
import threading
import multiprocessing


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def find_primes(start=3, end=100):
    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    return primes


start_time = time.time()
primes1 = find_primes(3, 10000)
primes2 = find_primes(10001, 20000)
primes3 = find_primes(20001, 30000)
end_time = time.time()
sequential_time = end_time - start_time

start_time = time.time()
thread1 = threading.Thread(target=find_primes, args=(3, 10000))
thread2 = threading.Thread(target=find_primes, args=(10001, 20000))
thread3 = threading.Thread(target=find_primes, args=(20001, 30000))
thread1.start()
thread2.start()
thread3.start()
thread1.join()
thread2.join()
thread3.join()
end_time = time.time()
thread_time = end_time - start_time

start_time = time.time()
process1 = multiprocessing.Process(target=find_primes, args=(3, 10000))
process2 = multiprocessing.Process(target=find_primes, args=(10001, 20000))
process3 = multiprocessing.Process(target=find_primes, args=(20001, 30000))
process1.start()
process2.start()
process3.start()
process1.join()
process2.join()
process3.join()
end_time = time.time()
process_time = end_time - start_time

print("Sequential Execution Time:", sequential_time)
print("Thread Execution Time:", thread_time)
print("Process Execution Time:", process_time)
