import threading
import random
import time


# IO-bound - задачи, связанные с ожиданием данных, ввода-вывода - потоки обеспечивают преимущество,
# реализуя конкурентность

class MyThread(threading.Thread):
    def __init__(self, number):
        threading.Thread.__init__(self)
        self.number = number

    def run(self):
        # что-то долго вычисляем тем же способом
        print(f'Старт вычислений №{self.number}')
        sleeping = random.randint(1, 5)
        time.sleep(sleeping)
        print(f'Конец вычислений №{self.number}. Затрачено {sleeping} секунд')


# Результат практически тот же самый, но в новом потоке будет запущен метод run.
start = time.perf_counter() # считаем что-то много раз с разными параметрами
threads = []
for i in range(5):  # os.cpu_count() - 1
    thr = MyThread(i)
    thr.start()
    threads.append(thr)

for thr in threads:
    thr.join()
print(f'Общее время вычислений в секундах: {int(time.perf_counter() - start)}')
