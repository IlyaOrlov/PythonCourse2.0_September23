import time
import random


class Pupil:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    thinking_time = random.randint(3, 6)
    time.sleep(thinking_time)

    def info(self):
        print(f"Имя ученика - {self.name}, " f"возраст - {self.age}")


x = Pupil("Иван", 8)
x.info()
