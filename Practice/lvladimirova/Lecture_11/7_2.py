from time import sleep
from random import randint


class Man:
    def __init__(self, name):
        self._name = name

    @staticmethod
    def solve_task():
        print("I'm not ready yet")

    def show(self):
        print(f"{self._name}")


class Pupil(Man):
    @staticmethod  # благодаря сегодняшней лекции я поняла как это сделать :)
    def solve_task():
        sleep(randint(3, 6))
        super(Pupil, Pupil).solve_task()


if __name__ == "__main__":
    people = Man("Иван")
    people.show()
    people.solve_task()
    people2 = Pupil("Дмитрий")
    people2.show()
    people2.solve_task()
