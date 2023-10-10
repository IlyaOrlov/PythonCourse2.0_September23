# Написать класс Pupil, у которого переопределен метод solve_task.
# На этот раз он будет думать от 3 до 6 секунд (c помощью метода sleep библиотеки time и randint библиотеки random).
import time
import random


class Man:
    def __init__(self, name):
        self._name = name

    def solve_task(self):
        print("I'm not ready yet")

class Pupil(Man):
    def __init__(self, name, student):
        self._name = name
        self._student = student

stud = Pupil("Иван", "физики")
print(f"{stud._name}, направление {stud._student}")
i = random.randint(3,6)
time.sleep(i)
stud.solve_task()
