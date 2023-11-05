import threading
import time
from func_for10 import find_primes


st = time.perf_counter()
threads = []
arg = [1, 10001, 20001]
for n in arg:
    pr = threading.Thread(target=find_primes, args=(n, n+9999))
    pr.start()
    threads.append(pr)

for pr in threads:
    pr.join()
print(f'Затрачено на выполнение {time.perf_counter() - st:.2f} sec.')

# Время выполнения 5.62 секунд
# Если 'забыть' выполнить start для потоков, то потоки не начнут выполнять свои операции.
# Если 'забыть' выполнить join для потоков, то главный поток не будет ждать окончания выполнения операции
# определенного дочернего потока, а во время его работы может начать работу другой поток.
# Потоки не дают преимуществ в задачах CPU-bound (и в данной вычислительной задаче), поскольку GIL блокирует
# одновременную работу нескольких потоков.
