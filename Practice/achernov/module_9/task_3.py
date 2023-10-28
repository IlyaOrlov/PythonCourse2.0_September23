import time


class MyCtxTime:

    def __enter__(self):
        self.start_time = time.time()
        print("Начало исполнения кода")

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end_time = time.time()
        print(f"Код закончил своё выполнение за {self.end_time - self.start_time}")


with MyCtxTime():
    time.sleep(1)

