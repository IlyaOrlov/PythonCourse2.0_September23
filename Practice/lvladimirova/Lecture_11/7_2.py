import random
import time


class Man:
    def __init__(self, name):
        self.name = name

    @staticmethod
    def solve_task():
        print("I'm not ready yet")

    def show(self):
        print(f"{self.name}")


class Pupil(Man):

    def solve_task(self):
        super().solve_task()
        time.sleep(random.randint(3, 6))


if __name__ == "__main__":
    people = Man("Иван")
    people.show()
    people.solve_task()
    people2 = Pupil("Дмитрий")
    people2.show()
    people2.solve_task()
