import time
import threading
import multiprocessing
from math import sqrt


def find_primes(end, start=3):
    lst = []
    for i in range(start, end + 1):
        for k in range(2, int(sqrt(i) + 1)):
            if i % k == 0:
                break
        else:
            lst.append(i)
    print(f"{lst}\n")


if __name__ == "__main__":

    start_time = time.perf_counter()
    find_primes(10000)
    find_primes(20000, 10001)
    find_primes(30000, 20001)
    print(f"Затрачено на последовательное выполнение: {time.perf_counter() - start_time} сек.")

    print("==========================================================================================")

    start_time = time.perf_counter()
    p = []
    for args in ((10000,), (20000, 10001), (30000, 20001)):
        thr = threading.Thread(target=find_primes, args=args)
        thr.start()
        p.append(thr)
    for n in p:
        n.join()
    print(f"Затрачено на параллельное выполнение потоками: {time.perf_counter() - start_time} сек.")

    print("==========================================================================================")

    start_time = time.perf_counter()
    p1 = []
    for args in ((10000,), (20000, 10001), (30000, 20001)):
        pr = multiprocessing.Process(target=find_primes, args=args)
        pr.start()
        p1.append(pr)
    for m in p1:
        m.join()
    print(f"Затрачено на параллельное выполнение процессами: {time.perf_counter() - start_time} сек.")

# Если 'забыть' выполнить start для потоков, то поток не запустится, т.е. программа выполняться не будет.
# Если 'забыть' выполнить join для потоков, то основная программа может завершиться раньше,
# чем завершится поток. С методом join потоки завершаются явно и в предсказуемый момент.
# Больше всего времени затрачено на параллельное выполнение через процессы из-за расходов,
# связанных с созданием и разделением ресурсов процессов (процессы имеют собственные области памяти,
# поэтому передача данных между ними может быть затратной).
# Последовательное и параллельное выполнение через потоки затрачивают примерно одинаковое время.
# Параллельное выполнение через потоки не даёт преимуществ в вычислительных задачах, так как
# GIL блокирует одновременную работу нескольких потоков.
