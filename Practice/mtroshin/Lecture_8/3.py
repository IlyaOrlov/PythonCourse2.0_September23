class ATM(object):
    def __init__(self, balance):
        self.__balance = balance


    def __repr__(self):
        return f'Тип банкомата = {type(self).__name__},\nБаланс = {self.balance},\nПоддерживаемые операции:{self.info()}'
    @property
    def balance(self):
        return self.__balance

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            return print(f"Баланс: {self.balance}")
        else:
            return print("Недостаточно средств.")

    def deposit(self, amount):
        new_balance = self.balance + amount
        if new_balance > 0:
            self.__balance = new_balance
            return print(f"Остаток: {self.balance}")
        else:
            return print("Ошибка!")

    def info(self):
        return "вывод/внесение средств"


class OnlineATM(ATM):
    def online_pay(self, amount):
        return print(f"Онлайн платеж совершен на сумму: {amount}")

    def info(self):
        return "вывод/внесение средств и онлайн платежи"


cash_machines = [ATM(100), OnlineATM(500)]

for atm in cash_machines:
    print(f"{atm}")

cash_machines[1].deposit(200)
cash_machines[1].deposit(500)
cash_machines[1].info()
cash_machines[1].online_pay(200)
