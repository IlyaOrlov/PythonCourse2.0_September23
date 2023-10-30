import time
import threading


# CPU-bound - потоки не дают преимущества

def count(n):
    while n > 0:
        n -= 1


c = 160000000
start = time.perf_counter()

half = c // 2
t1 = threading.Thread(target=count, args=(half,))
t2 = threading.Thread(target=count, args=(half,))
t1.start()
t2.start()
t1.join()
t2.join()
print(f'{time.perf_counter() - start:.2f} sec.')
