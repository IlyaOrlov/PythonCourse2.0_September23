class Employee:
    company = "OOO Super"

    def __init__(self, name, surname, salary):
        self.name = name
        self.surname = surname
        self.salary = salary
        self.car = None

    def print_emp(self):
        print(f"Employee at {id(self)}: {self.name=}, {self.surname=}, {self.salary=}")

    @staticmethod
    def say_hello():
        print("Hello")


e = Employee("Petr", "Petrov", 10000)
e.car = "Москвич"
print(f"{id(e)=}, {type(e)=}")
print(e.name)
print(e.surname)
print(e.salary)
print(e.car)

e1 = Employee("Semen", "Semenov", 50000)

# Employee.print_emp(e)
e.print_emp()  # Employee.print_emp(e)
e1.print_emp()  # Employee.print_emp(e1)

e.say_hello()  # => Employee.say_hello(e)
e1.say_hello()  # => Employee.say_hello(e)



