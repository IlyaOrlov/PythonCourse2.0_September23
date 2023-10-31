class User:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, new_age):
        self._age = new_age


class Worker(User):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self._salary = salary

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, new_salary):
        self._salary = new_salary

    def info(self):
        print(f'Name {self._name}, Age {self._age}, Solary {self._salary}')


if __name__ == "__main__":
    work1 = Worker("John", 25, 1000)
    work2 = Worker("Jack", 26, 2000)
    print(work1.salary + work2.salary)
