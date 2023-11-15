import time


class MyCtxTime:

    def __enter__(self):
        self._start_time = time.time()
        print("Начало исполнения кода")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Код закончил своё выполнение за {time.time() - self._start_time}")


with MyCtxTime():
    time.sleep(1)
