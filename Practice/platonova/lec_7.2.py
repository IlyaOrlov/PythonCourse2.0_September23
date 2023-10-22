import time
import random


class Man:
    def __init__(self, name):
        self.name = name

    def solve_task():
        print("I'm not ready yet")


class Pupil(Man):
    def solve_task(self):
        thinking_time = random.randint(3, 6)
        time.sleep(thinking_time)
        print("I'm not ready yet")


x = Pupil("Иван")
x.solve_task()