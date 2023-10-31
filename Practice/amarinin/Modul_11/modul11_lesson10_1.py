import multiprocessing
import threading
import time


def find_primes_step_1(start, end):
    lst_prime = []
    tim_start = time.time()
    for num in range(start, end + 1):
        for i in range(2, num, 1):
            if num % i == 0:
                break
            if i == num - 1:
                lst_prime.append(num)
    print(tim := round(time.time() - tim_start, 2), end="   ")
    return [lst_prime, tim]


if __name__ == "__main__":
    tim_start = time.time()
    find_primes_step_1(3, 10000)
    find_primes_step_1(10001, 20000)
    find_primes_step_1(20001, 30000)
    print(f"общее время {round(time.time() - tim_start, 2)}")

    tim_start = time.time()
    thread1 = threading.Thread(target=find_primes_step_1, args=(3, 10000))
    thread1.start()
    thread2 = threading.Thread(target=find_primes_step_1, args=(10001, 20000))
    thread2.start()
    thread3 = threading.Thread(target=find_primes_step_1, args=(20001, 30000))
    thread3.start()
    thread1.join()
    thread2.join()
    thread3.join()
    print(f"общее время {round(time.time() - tim_start, 2)}")

    tim_start = time.time()
    mult1 = multiprocessing.Process(target=find_primes_step_1, args=(3, 10000))
    mult1.start()
    mult2 = multiprocessing.Process(target=find_primes_step_1, args=(10001, 20000))
    mult2.start()
    mult3 = multiprocessing.Process(target=find_primes_step_1, args=(20001, 30000))
    mult3.start()
    mult1.join()
    mult2.join()
    mult3.join()
    print(f"общее время {round(time.time() - tim_start, 2)}")
