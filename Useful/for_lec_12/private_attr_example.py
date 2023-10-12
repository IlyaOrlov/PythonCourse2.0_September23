class Employee:
    def __init__(self, name):
        self.__name = name  # self._Employee__name

    def say_hello(self):
        print(f"Hello! I'm {self.__name}")  # self._Employee__name


class Manager(Employee):
    def say_hello(self):
        print(f"Hello! I'm manager {self.__name}")  # self._Manager__name


m = Manager("Ivan")
m.say_hello()
# print(m.__name)

