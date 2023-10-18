import time


def big(text):
    txt = ""
    for i, n in enumerate(text, 1):
        if i % 2 == 0:
            txt += n.upper()
            i += 1
        else:
            txt += n
            i += 1
    return txt


class Clock:
    def __enter__(self):
        self._start = time.time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._end = time.time()
        d = self._end - self._start
        print(f"Время исполнения кода: {d}")


t = "Хорошо живет на свете Винни-Пух"
with Clock():
    b = big(t)
    print(b)
