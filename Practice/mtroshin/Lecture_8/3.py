class ATM(object):
    def __init__(self, balance):
        self.__balance = balance

    def __repr__(self):
        return f'Тип банкомата = {type(self).__name__},\nБаланс = {self.balance},\nПоддерживаемые операции:{self.info()} и {self.deposit(100)}'

    @property
    def balance(self):
        return self.__balance

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            return f"Баланс: {self.balance}"
        else:
            return "Недостаточно средств."

    def deposit(self, amount):
        new_balance = self.balance + amount
        if new_balance > 0:
            self.__balance = new_balance
            return f"Остаток: {self.balance}"
        else:
            return "Ошибка!"

    def info(self):
        return "вывод/внесение средств"

    def online_pay(self, amount):
        return ""


class OnlineATM(ATM):
    def online_pay(self, amount):
        return f"Онлайн платеж совершен на сумму: {amount}"

    def info(self):
        return "вывод/внесение средств и онлайн платежи"


cash_machines = [ATM(100), OnlineATM(500)]

for atm in cash_machines:
    print(f"{atm}\nВнесли 11. {atm.deposit(11)}\nСняли 21. {atm.withdraw(21)}\n{atm.online_pay(111)}\n")

