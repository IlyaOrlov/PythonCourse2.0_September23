import random
import threading
import random


def hold(data):
    data = random.randint(1, 100)
    local.value = data
    print(f'Имя потока: {threading.current_thread().name}, хранит данные: {local.value}')


local = threading.local()
threads = []
for i in range(3):
    thr = threading.Thread(target=hold, args=(local,))
    thr.start()
    threads.append(thr)

for thr in threads:
    thr.join()
