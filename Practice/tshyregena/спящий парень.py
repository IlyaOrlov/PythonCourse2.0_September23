import time
import random


class Man:
    def __init__(self, name):
        self.name = name

    @staticmethod
    def solve_task(self):
        print(f"I'm not ready yet")


class Pupil(Man):

    @staticmethod
    def solve_task(self):
        r = random.randrange(3, 6)
        time.sleep(r)
        print(f"Я подумал {r} секунды, но я тоже не готов пока.")


m = Man("Гоша")
m.solve_task(m)
h = Pupil("Лев")
h.solve_task(h)
