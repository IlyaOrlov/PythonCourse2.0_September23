class Bank:

    def __init__(self, name, money):
        self.name = name
        self._money = money
        print(f"Создан {self.name} с балансом на счету {self._money}")

    @staticmethod
    def info():
        print("Этот банкомат умеет только снимать и пополнять наличные")

    def deposit_in(self, cash):
        self._money += cash

    def deposit_out(self, cash):
        if cash <= self._money:
            self._money -= cash
        else:
            print("Недостаточно средств")

    def show(self):
        print(f"Баланс равен {self._money}")

    @property
    def money(self):
        return self._money


class Bank2(Bank):

    @staticmethod
    def info():
        print("Банкомат умеет снимать, пополнять и переводить деньги онлайн")

    def sbp(self, sbp):
        if sbp <= self._money:
            self._money -= sbp
            return f"Перевод осуществлён на сумму {sbp}. Баланс : {self.money}"
        else:
            print("Недостаточно средств")


bank1 = Bank("первыйБанк", 10000)
bank2 = Bank("второйБанк", 20000)
bank3 = Bank2("третийБанк", 30000)
banks = [bank1, bank2, bank3]
for i in banks:
    print(f"У банка {i.name} баланс: {i.money}")
    i.info()
    i.deposit_in(5000)
    i.deposit_out(2000)
    print(f"У банка {i.name} осталось: {i.money}")
print(bank3.sbp(10000))
