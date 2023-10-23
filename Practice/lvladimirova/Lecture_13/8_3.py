import time


class Time:
    def __enter__(self):
        self._start = time.time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        stop = time.time()
        print(f"Время выполнения кода = {stop - self._start} сек")


if __name__ == "__main__":
    with Time():
        s = input("Введите пятизначное число: ")
        if len(s) == 5 and s.isdecimal():
            print(f"Число:{s}")
            for i, x in enumerate(s, 1):
                print(f"{i} цифра равна {x}")
        else:
            print("Вы ввели не пятизначное число!")
