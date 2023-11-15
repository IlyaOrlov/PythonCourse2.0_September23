import time
import threading
import multiprocessing


def find_primes(*args):
    if len(args) == 2:
        start = args[0]
        end = args[1]
    else:
        start = 3
        end = args[0]

    pr_num = []
    for i in range(start, end + 1):
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                break
        else:
            pr_num.append(i)
    return pr_num


if __name__ == "__main__":
    par = (3, 10000, 10001, 20000, 20001, 30000)

    s_time = time.perf_counter()
    i = 0
    while i < len(par) - 1:
        find_primes(par[i], par[i + 1])
        i += 2
    print("Sequential Execution Time: {round(time.perf_counter() - s_time, 2)}")

    s_time = time.perf_counter()
    threads = []
    i = 0
    while i < len(par) - 1:
        thr = threading.Thread(target=find_primes, args=(par[i], par[i + 1]))
        thr.start()
        threads.append(thr)
        i += 2

    for thr in threads:
        thr.join()

    print(f"Thread Execution Time: {round(time.perf_counter() - s_time, 2)}")

    s_time = time.perf_counter()
    processes = []
    i = 0
    while i < len(par) - 1:
        p = multiprocessing.Process(target=find_primes, args=(par[i], par[i + 1]))
        p.start()
        processes.append(p)
        i += 2

    for p in processes:
        p.join()

    print(f"Process Execution Time: {round(time.perf_counter() - s_time, 2)}")
