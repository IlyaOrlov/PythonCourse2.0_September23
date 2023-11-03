import time
import threading
import multiprocessing


def find_primes(end, start=3):
    lst = []
    for i in range(start, end + 1, 2):
        if (i > 10) and (i % 10 == 5):
            continue
        for j in lst:
            if j * j - 1 > i:
                lst.append(i)
                break
            if i % j == 0:
                break
        else:
            lst.append(i)
    return lst


if __name__ == "__main__":

    start_time = time.perf_counter()
    find_primes(10000)
    find_primes(20000, 10001)
    find_primes(30000, 20001)
    print(f"Затрачено времени на последовательное выполнение:"
          f" {time.perf_counter() - start_time} сек")

    start_time = time.perf_counter()
    t = []
    for args in ((10000,), (20000, 10001), (30000, 20001)):
        thr = threading.Thread(target=find_primes, args=args)
        thr.start()
        t.append(thr)
    for n in t:
        n.join()
    print(f"Затрачено времени на паралле-ое выпол-е потоками:"
          f" {time.perf_counter() - start_time} сек")

    start_time = time.perf_counter()
    p = []
    for args in ((10000,), (20000, 10001), (30000, 20001)):
        pr = multiprocessing.Process(target=find_primes, args=args)
        pr.start()
        p.append(pr)
    for m in p:
        m.join()
    print(f"Затрачено времени на паралле-ое выпол-е процессами:"
          f" {time.perf_counter() - start_time} сек")

# Если 'забыть' выполнить start для потоков, поток не запустится.
# Программа выполняться не будет, так как функция запущена в потоке.
# Если 'забыть' выполнить join для потоков, то может быть такое, что основная программа завершится,
# а поток продолжится. С методом join потоки завершаются явно и в предсказуемый момент.
# И удаляет из памяти со всем своим стеком.
# В процессах думаю то же самое.
# Время выполнения больше всего через процессы. Это происходит из-за накладных расходов,
# связанных с созданием и разделением ресурсов процессов, включая память. Также процессы
# имеют свои собственные области памяти, поэтому передача данных между процессами может быть более затратной.
# Последовательное выполнение и параллельное через потоки примерно одинаковое. У потоков нет большего преимущества,
# если оно вообще есть, из-за Gil(в вычислительных задачах не дают преимущества).
