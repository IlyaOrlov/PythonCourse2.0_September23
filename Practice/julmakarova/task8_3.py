import time


class TimeManager:
    def __enter__(self):
        self._start = time.time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        stop = time.time()
        print(f"Время выполнения данного кода: {stop - self._start} c.")


with TimeManager():
    n = int(input("Введите целое число: "))
    lst = [n ** i for i in range(5)]
    print(lst)
