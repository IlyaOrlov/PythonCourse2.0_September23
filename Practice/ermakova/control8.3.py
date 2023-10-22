import time
import random


class Timer:
    def __enter__(self):
        self.start = time.time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.stop = time.time()
        print(f"Время выполнения вашего кода:{self.stop-self.start} сек")


with Timer():
    n = int(input("Ввведите число: "))
    lst = [random.randint(-10, 10) for i in range(n)]
    print(lst)
    print(f"Минимум вашего списка равен {min(lst)}")
