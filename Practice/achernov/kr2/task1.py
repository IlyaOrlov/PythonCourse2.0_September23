class User:

    def __init__(self, name, age):
        self._name = name
        self._age = age

    def set_name(self):
        pass

    def get_name(self):
        pass

    def set_age(self):
        pass

    def get_age(self):
        pass


class Worker(User):

    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self._salary = salary

    def get_salary(self):
        pass

    def set_salary(self):
        pass

    @property
    def salary(self):
        return self._salary


w1 = Worker("John", 25, 1000)
w2 = Worker("Jack", 26, 2000)
res = w1.salary + w2.salary
print(res)
