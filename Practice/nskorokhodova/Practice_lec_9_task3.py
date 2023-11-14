import time


class MyTime:
    def __enter__(self):
        self._start_time = time.time()
        print("Начало исполнения кода")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Время исполнения {time.time() - self._start_time}")


with MyTime():
    time.sleep(1)
