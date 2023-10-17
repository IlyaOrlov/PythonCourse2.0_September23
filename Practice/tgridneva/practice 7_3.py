class ATM:
    def __init__(self, cash):
        self._cash = cash

    def get_cash(self, amount):
        if amount <= self._cash:
            self._cash -= amount
            print(f"Withdrew {amount} cash")
        else:
            print("Insufficient cash")

    def deposit_cash(self, amount):
        self._cash += amount
        print(f"Deposited {amount} cash")

    def get_supported_operations(self):
        return ["Withdraw Cash", "Deposit Cash"]

    def make_payment(self, amount):
        pass


class OnlineATM(ATM):

    def make_payment(self, amount):
        print(f"Made a payment of {amount}")

    def get_supported_operations(self):
        return super().get_supported_operations() + ["Make Payment"]


atm1 = ATM(1000)
atm2 = OnlineATM(2000)

atms = [atm1, atm2]

for atm in atms:
    print(f"ATM Cash: {atm._cash}")
    print(f"Supported Operations: {atm.get_supported_operations()}")

    atm.get_cash(500)
    atm.deposit_cash(1000)

    if isinstance(atm, OnlineATM):
        atm.make_payment(300)

    print(f"ATM Cash: {atm._cash}")
    print("------------------------")
