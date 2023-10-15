class Employee:
    def __init__(self, name, surname, salary):
        self._name = name
        self._surname = surname
        self._salary = salary

    @property
    def name(self):
        return f"{self._name} {self._surname}"

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, new_salary):
        self._salary = new_salary

    def show(self):
        print(f"{self.name} with salary = {self.salary}")


class Manager(Employee):
    def __init__(self, name, surname, salary):
        super().__init__(name, surname, salary)
        self._emps = []

    def add_emp(self, new_emp):
        if isinstance(new_emp, Employee):
            self._emps.append(new_emp)
        else:
            print("Ошибка!")
        return self

    def __add__(self, new_emp):
        if isinstance(new_emp, Employee):
            self._emps.append(new_emp)
        else:
            print("Ошибка!")
        return self

    def show(self):
        print(f"{self.name} with salary = {self.salary} and emps: {self._emps}")


e1 = Employee("Иван", "Иванов", 100000)
e2 = Employee("Петр", "Петров", 100000)
m = Manager("Аристарх", "Тапкин", 200000)
for e in (e1, e2, m):
    e.show()

m.add_emp(e1)
m.show()
