class Employee:
    def __init__(self, name, surname, salary):
        self.name = name
        self.surname = surname
        self.salary = salary
        self.car = None

    def print_emp(self):
        print(f"Employee at {id(self)}: {self.name=}, {self.surname=}, {self.salary=}")

    # def add(self, another_emp):
    #     return self.salary + another_emp.salary

    def __add__(self, other):
        new_salary = self.salary + other.salary
        new_emp = Employee(None, None, new_salary)
        return new_emp




e = Employee("Петр", "Петров", 10000)
e.print_emp()

e1 = Employee("Аристарх", "Тапкин", 20000)
e1.print_emp()

s = e + e1  # e.__add__(e1)
print(s.salary)
