import time
import random


class Man:
    def __init__(self, name):
        self._name = name

    @staticmethod
    def solve_task():
        print("I'm not ready yet")


class Pupil(Man):
    @staticmethod
    def solve_task():
        time.sleep(random.randint(3, 6))
        super(Pupil, Pupil).solve_task() # как я поняла, super() со статическим методом работает только в такой интерпретации
                                         # спасибо stackoverflow:) ну либо прописывать явно Man.solve_task()


m = Man("Mihail")
m.solve_task()

p = Pupil("Valeriy")
p.solve_task()


