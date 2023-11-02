import multiprocessing
import threading
import time


def find_primes_step_1(start, end):
    lst_prime = []
    t_start = time.time()
    for num in range(start, end + 1):
        for i in range(2, int(num ** 0.5), 1):
            if num % i == 0:
                break
        else:
            lst_prime.append(num)
    tim = round(time.time() - t_start, 3)
    str(tim).ljust(5, "0")
    print(str(tim).ljust(5, "0"), end="   ")


if __name__ == "__main__":
    data = [(3, 100000), (100001, 200000), (200001, 300000)]

    res1 = []
    tim_start = time.time()
    for dt in data:
        find_primes_step_1(dt[0], dt[1])
    tim_total = str(round(time.time() - tim_start, 3)).ljust(5, '0')
    print(f"общее время {tim_total} ")

    res2 = []
    tim_start = time.time()
    for dt in data:
        th = threading.Thread(target=find_primes_step_1, args=(dt[0], dt[1]))
        th.start()
        res2.append(th)
    for th in res2:
        th.join()
    tim_total = str(round(time.time() - tim_start, 3)).ljust(5, '0')
    print(f"общее время {tim_total} ")

    res3 = []
    tim_start = time.time()
    for dt in data:
        mult = multiprocessing.Process(target=find_primes_step_1, args=(dt[0], dt[1]))
        mult.start()
        res3.append(mult)
    for mult in res3:
        mult.join()
    tim_total = str(round(time.time() - tim_start, 3)).ljust(5, '0')
    print(f"общее время {tim_total} ")

#  Если не выполнить функцию start(), но выполнить join(), будет выброшена ошибка
#  AssertionError: can only join a started process
#  Eсли запустить функцию start(), но не выполнить join(), интерпретатор не будет ждать
#  завершение обозначенного потока или процесса и при возможности продолжит
#  выполнение основного потока или просесса. И это может привести к наружению логики
#  и непредсказуемости результата. появляется ассинхронность.
