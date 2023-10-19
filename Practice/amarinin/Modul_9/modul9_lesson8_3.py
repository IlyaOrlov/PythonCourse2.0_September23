import time


class TestManager:
    def __enter__(self):
        print("Время пошло :")
        self.start = time.time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Время вышло : {round(time.time() - self.start, 3)} сек.")


if __name__ == "__main__":
    with TestManager():
        for a in range(10050):
            b = a ** a
