class Employee:
    company = "OOO Super"

    @classmethod
    def change_company(cls, new_company_name):
        if type(new_company_name) == str:
            cls.company = new_company_name
        else:
            print("Ошибка!")


class ITEmployee(Employee):
    pass

class BankEmployee(Employee):
    pass


ITEmployee.change_company("IT company")
BankEmployee.change_company("MegaBank")

print(ITEmployee.company)
print(BankEmployee.company)
