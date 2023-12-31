from time import sleep
from random import randint


class Man:

    def __init__(self, name="Mans"):
        self._name = name

    @staticmethod
    def solve_task():
        print("I`m not ready yet")


class Pupil(Man):

    def __init__(self, name="Pupil"):
        super().__init__(name)

    @staticmethod
    def solve_task():
        print("0", end="->")
        for i in range(randint(3, 6)):
            sleep(1)
            print(f"{i + 1}", end="->")
        super(Pupil, Pupil).solve_task()


if __name__ == "__main__":
    pup = Pupil()
    pup.solve_task()
