import threading
import random


def info_thread(i):
    print(f"{threading.current_thread().name} имеет секретное число = {i}")


threads = []

for i in range(2):
    pr_data = random.randint(1, 5)
    th = threading.Thread(name="Поток "+str(i), target=info_thread, args=(pr_data,))
    th.start()
    threads.append(th)

for t in threads:
    t.join()
