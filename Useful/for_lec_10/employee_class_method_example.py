class Employee:
    company = "OOO Super"

    def __init__(self, name, surname, salary):
        self.name = name
        self.surname = surname
        self.salary = salary
        self.car = None

    def print_emp(self):
        print(f"Employee at {id(self)}: {self.name=}, {self.surname=}, {self.salary=}")

    @classmethod
    def change_company(cls, new_company_name):
        if type(new_company_name) == str:
            cls.company = new_company_name
        else:
            print("Ошибка!")


    @staticmethod
    def say_hello():
        print("Hello")


Employee.change_company(123)

e = Employee("Petr", "Petrov", 10000)
e.car = "Москвич"
print(f"{id(e)=}, {type(e)=}")
print(e.name)
print(e.surname)
print(e.salary)
print(e.car)
print(e.company)
