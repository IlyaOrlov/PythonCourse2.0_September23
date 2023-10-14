class EmployeeSalaryError(Exception):
    pass


class Employee:
    def __init__(self, name, surname, salary):
        self._name = name
        self._surname = surname
        if isinstance(salary, int):
            self._salary = salary
        else:
            raise EmployeeSalaryError(f"Exception: incorrect salary type {type(salary)}")

    @property
    def salary(self):
        return self._salary

    def add_salary(self, bonus):
        if isinstance(bonus, int):
            self._salary += bonus
            return True
        else:
            print("Ошибка")
            return False


e = Employee(
    name=input("Введите имя: "),
    surname=input("Введите фамилию: "),
    salary=input("Введите з/п: ")
)

if not e.add_salary(50000):
    exit(1)

print(f"{e.salary=}")
