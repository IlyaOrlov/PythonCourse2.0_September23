class User:

    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        print("геттер")
        return self._name

    @name.setter
    def name(self, new_name):
        print("сеттер")
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


w1 = Worker("John", 25, 1000)
w2 = Worker("Jack", 26, 2000)
res = w1.salary + w2.salary
print(f"Суммарная зп = {res} баксов")
