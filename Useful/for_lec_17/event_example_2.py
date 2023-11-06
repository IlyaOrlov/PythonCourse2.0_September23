import threading
import random
import time


def compute(number, ev):
    # что-то долго вычисляем тем же способом
    print(f'Старт вычислений №{number}')
    sleeping = random.randint(1, 5)
    time.sleep(sleeping)
    print(f'Конец вычислений №{number}. Затрачено {sleeping} секунд')
    ev.set()


start = time.perf_counter() # считаем что-то много раз с разными параметрами
threads = []
for i in range(5):
    ev = threading.Event()
    thr = threading.Thread(target=compute, args=(i,ev))
    thr.start()
    threads.append((thr, ev))


num_of_events = 0
while num_of_events < len(threads):
    num_of_events = 0
    for _, ev in threads:
        if ev.is_set():
            num_of_events += 1

for thr, _ in threads:
    thr.join()
print(f'Общее время вычислений в секундах: {int(time.perf_counter() - start)}')
