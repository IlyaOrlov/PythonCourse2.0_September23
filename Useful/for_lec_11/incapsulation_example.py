class Employee:
    def __init__(self, name, salary):
        self.__name = name  # self._Employee__name
        self.__salary = salary  # self._Employee__salary

    @property
    def name(self):
        return self.__name

    @property
    def salary(self):
        return self.__salary


e = Employee("Иван", 100500)
print(e.__dict__)
print(e.name)
print(e.salary)
