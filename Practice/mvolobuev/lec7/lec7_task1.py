# Написать класс Man, который принимает имя в конструкторе.
# Имеет метод solve_task, который просто выводит "I'm not ready yet".

class Man:
    def __init__(self, name):
        self._name = name

    def solve_task(self):
        print("I'm not ready yet")


imy = Man("Святослав")
print(imy._name)
imy.solve_task()
