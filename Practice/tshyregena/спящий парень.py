import time
import random


class Man:
    def __init__(self, name):
        self.name = name

    @staticmethod
    def solve_task():
        print(f"I'm not ready yet")


class Pupil(Man):

    @staticmethod
    def solve_task():
        r = random.randrange(3, 6)
        time.sleep(r)
        print(f"Я подумал {r} секунды, но я тоже не готов пока.")


m = Man("Гоша")
m.solve_task()
h = Pupil("Лев")
h.solve_task()
