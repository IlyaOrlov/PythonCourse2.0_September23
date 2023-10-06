class Employee:
    def __init__(self, name, surname, salary):
        self.name = name
        self.surname = surname
        self._salary = salary
        self.car = None

    def __add__(self, other):
        return Employee(None, None, self.salary + other.salary)

    def __str__(self):
        return f"Employee: {self.name=}, {self.surname=}, {self.salary=}"

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, new_salary):
        if isinstance(new_salary, int):
            self._salary = new_salary
        else:
            print("Ошибка!")


e1 = Employee("Петр", "Петров", 10000)
e2 = Employee("Аристарх", "Тапкин", 20000)

print(e1.salary)

e1.salary = input("Введите новую з/п: ")
e2.salary = input("Введите новую з/п: ")

# f = e1 + e2
# print(f.salary)
