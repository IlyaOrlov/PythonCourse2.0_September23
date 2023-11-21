import time
from func_for10 import find_primes


st = time.perf_counter()
pr1 = find_primes(1, 10000)
pr2 = find_primes(10001, 20000)
pr3 = find_primes(20001, 30000)
print(f'Затрачено на выполнение {time.perf_counter() - st:.2f} sec.')
# Время последовательного выполнения 5.54 секунд
