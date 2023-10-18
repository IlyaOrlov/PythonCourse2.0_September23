import time


class TestManager:
    def __init__(self):
        self.start = time.time()

    def __enter__(self):
        print("Время пошло :")

    def __exit__(self, exc_type, exc_val, exc_tb):
        tims = round(time.time() - self.start, 3)
        print(f"Время вышло : {tims} сек.")


if __name__ == "__main__":
    with TestManager():
        for a in range(10050):
            b = a ** a
