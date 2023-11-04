import multiprocessing
import threading
import time


def find_primes(start, end):
    if start <= 2:
        primes = [2]
        start = 3
    else:
        primes = []
    for num in range(start, end + 1, 2):
        if all(num % i != 0 for i in range(2, int(num**0.5) + 1)):
            primes.append(num)
    print(f"Простые числа в диапазоне от {start} до {end}: {primes}")
    return primes


if __name__ == "__main__":
    # print(find_primes(3, 10000))
    # print(find_primes(10001, 20000))
    # print(find_primes(20001, 30000))

    start_time = time.time()
    primes1 = find_primes(3, 10000)
    primes2 = find_primes(10001, 20000)
    primes3 = find_primes(20001, 30000)
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Последовательное выполнение: {execution_time} сек.")

    print("==========================")

    start_time = time.time()

    threads = []
    for x in range(3, 30001, 10000):
        y = x + 9999
        thr = threading.Thread(target=find_primes, args=(x, y))
        thr.start()
        threads.append(thr)

    for thr in threads:
        thr.join()

    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Параллельное выполнение потоков: {execution_time} сек.")

    print("==========================")

    start_time = time.time()

    process = []
    for x in range(3, 30001, 10000):
        y = x + 9999
        prc = multiprocessing.Process(target=find_primes, args=(x, y))
        prc.start()
        process.append(prc)

    for prc in process:
        prc.join()

    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Параллельное выполнение процессов: {execution_time} сек.")
