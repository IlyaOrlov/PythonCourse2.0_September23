class Atm:
    _functional = "only cash transactions"

    def __init__(self, cash):
        self._cash = cash

    @property
    def cash(self):
        return self._cash

    @cash.setter
    def cash(self, new_cash):
        if isinstance(new_cash, int):
            self._cash = new_cash
        else:
            print("Transaction error!")

    @property
    def functional(self):
        return self._functional

    def __str__(self):
        return f"This ATM {self.functional}. Amount of cash: {self.cash}. "

    def add_cash(self, money):
        self.cash += money
        print(f"Cash acceptance: {money} ")

    def sub_cash(self, money):
        result = self.cash - money
        if result >= 0:
            self.cash = result
            print(f"Cash withdrawal: {money} ")
        else:
            print(f"Insufficient funds!")


class AtmPay(Atm):
    _functional = "cash transactions and online pay"

    @staticmethod
    def pay(money):
        print(f"Online pay for the amount: {money}")


atm1 = Atm(100000)
print(atm1)
atm1.add_cash(20000)
print(atm1)
atm1.sub_cash(50000)

atm2 = AtmPay(50000)
atm2.add_cash(1500)
atm2.pay(10000)


lst_atm = [atm1, atm2, AtmPay(200000), Atm(500000), AtmPay(5000)]

for x in lst_atm:
    print(x)
