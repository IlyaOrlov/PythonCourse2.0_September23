class ATM(object):
    def __init__(self, balance):
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    def withdraw(self, amount):
        if amount <= self.balance:
            self._balance -= amount
            return print(f"Баланс: {self.balance}")
        else:
            return print("Недостаточно средств.")

    def deposit(self, amount):
        new_balance = self.balance + amount
        if new_balance > 0:
            self._balance = new_balance
            return print(f"Остаток: {self.balance}")
        else:
            return print("Ошибка!")

    def info(self):
        return print("вывод/внесение средств")

class OnlineATM(ATM):
    def online_pay(self, amount):
        if amount <= self.balance:
            self._balance -= amount
            return print(f"Остаток: {self.balance}")
        else:
            return print("Недостаточно средств.")

    def info(self):
        return print("вывод/внесение средств и онлайн платежи")


cash_machines = [ATM(100), OnlineATM(500)]

for atm in cash_machines:
    print(f"Тип банкомата: {atm},\nбаланс: {atm.balance}\nПоддерживаемые операции: {atm.info()}\n")

cash_machines[1].deposit(200)
cash_machines[1].deposit(500)
cash_machines[1].info()
cash_machines[1].online_pay(200)
