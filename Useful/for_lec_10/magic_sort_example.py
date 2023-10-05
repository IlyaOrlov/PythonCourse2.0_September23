class Employee:
    def __init__(self, name, surname, salary):
        self.name = name
        self.surname = surname
        self.salary = salary
        self.car = None

    def __str__(self):
        return f"Employee: {self.name=}, {self.surname=}, {self.salary=}"

    def __repr__(self):
        return f"Employee at {id(self)}: {self.name=}, {self.surname=}, {self.salary=}"

    def __gt__(self, other):
        if self.surname == other.surname:
            if self.name == other.name:
                return self.salary > other.salary
            else:
                return self.name > other.name
        else:
            return self.surname > other.surname


e1 = Employee("Петр", "Петров", 10000)
e2 = Employee("Аристарх", "Тапкин", 20000)
e3 = Employee("Семен", "Ложкин", 20000)
e4 = Employee("Геннадий", "Ложкин", 20000)
e5 = Employee("Геннадий", "Ложкин", 25000)
lst = [e1, e2, e3, e4, e5]
for e in lst:
    print(e)
# print(e1 > e2)
print("=============================")
lst.sort()
for e in lst:
    print(e)

