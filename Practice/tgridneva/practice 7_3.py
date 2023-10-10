class ATM:
    def __init__(self, balance):
        self._balance = balance

    def get_cash(self, amount):
        if amount <= self._balance:
            self._balance -= amount
            print(f"Withdrew {amount} cash")
        else:
            print("Insufficient balance")

    def deposit_cash(self, amount):
        self._balance += amount
        print(f"Deposited {amount} cash")

    def get_supported_operations(self):
        return ["Withdraw Cash", "Deposit Cash"]


class OnlineATM(ATM):
    def __init__(self, balance):
        super().__init__(balance)

    def make_payment(self, amount):
        if amount <= self._balance:
            self._balance -= amount
            print(f"Made a payment of {amount}")
        else:
            print("Insufficient balance")

    def get_supported_operations(self):
        return super().get_supported_operations() + ["Make Payment"]


atm1 = ATM(1000)
atm2 = OnlineATM(2000)

atms = [atm1, atm2]

for atm in atms:
    print(f"ATM Balance: {atm._balance}")
    print(f"Supported Operations: {atm.get_supported_operations()}")
    print("------------------------")

    atm.get_cash(500)
    atm.deposit_cash(1000)

    if isinstance(atm, OnlineATM):
        atm.make_payment(300)

    print(f"ATM Balance: {atm._balance}")
    print("------------------------")
