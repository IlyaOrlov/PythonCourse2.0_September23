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
        flag = True
        for j in range(2, int(i**0.5)+1):
            if i%j == 0:
                flag = False
                break
        if flag:
            pr_num.append(i)
    return pr_num


if __name__ == "__main__":
    par = (3, 10000, 10001, 20000, 20001, 30000)

    # Последовательный код
    s_time = time.perf_counter()
    i = 0
    while i < len(par) - 1:
        find_primes(par[i], par[i + 1])
        i += 2
    print(f"Время выполнения последовательного кода: {round(time.perf_counter() - s_time, 2)}")

    # Код с потоками
    s_time = time.perf_counter()
    threads = []
    i = 0
    while i < len(par) - 1:
        thr = threading.Thread(target=find_primes, args=(par[i], par[i + 1]))
        thr.start()
        threads.append(thr)
        i += 2

    # если забыть выполнить start(), то поток не запустится,
    # а в ходе выполнения кода вылетит ошибка RuntimeError: cannot join thread before it is started

    for thr in threads:
        thr.join()

    # если забыть выполнить join(), то главный поток может не дождаться завершения всех дочерних потоков
    # но в ходе выполнения кода мы не замечаем изменений, поскольку у интерпретатора предусмотрена подстраховка на этот счет

    print(f"Время выполнения кода по потокам: {round(time.perf_counter() - s_time, 2)}")

    # Код с процессами
    s_time = time.perf_counter()
    processes = []
    i = 0
    while i < len(par) - 1:
        p = multiprocessing.Process(target=find_primes, args=(par[i], par[i + 1]))
        p.start()
        processes.append(p)
        i += 2

    # если забыть выполнить start(), то процесс не будет запущен,
    # а в ходе выполнения кода вылетит ошибка RuntimeError: cannot join thread before it is started

    for p in processes:
        p.join()

    # если забыть выполнить join(), то программа не дожидается завершения всех дочерних процессов
    # и мы замечаем, что время выполнения становится заметно меньше, поскольку процессы не успели закончить свои вычисления

    print(f"Время выполнения кода по процессам: {round(time.perf_counter() - s_time, 2)}")

    # Выводы
    # По результатам сравнения времени выполнения каждого из блоков, можно сделать следующие выводы:
    # - распараллеливание по потокам не дает преимущества во времени в задачах CPU- bound (происходит это по причине
    #   GIL - глобальной блокировки интерпретатора (каждый из потоков полностью "захватывает" процессор для своего выполнения)
    # - распараллеливание по процессам также не дало преимуществ в данной задаче, поскольку расходы на создание процессов
    #   не "окупились", объемы вычислений не достаточно велики для вычисления в разных процессах
    #   При добавлении еще одного порядка (не 10 тысяч, а 100 и т.д.), разница становится ощутима (время выполнения
    #   последовательного кода практически в 2 раза превышает время выполнения кода по процессам
