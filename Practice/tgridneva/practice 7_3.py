class ATM:
    def __init__(self, cash):
        self.cash = cash

    def get_cash(self, amount):
        if amount <= self.cash:
            self.cash -= amount
            print(f"Withdrew {amount} cash")
        else:
            print("Insufficient cash")

    def deposit_cash(self, amount):
        self.cash += amount
        print(f"Deposited {amount} cash")

    def get_supported_operations(self):
        return ["Withdraw Cash", "Deposit Cash"]


class OnlineATM(ATM):
    def __init__(self, cash):
        super().__init__(cash)

    def make_payment(self, amount):
        if amount <= self.cash:
            self.cash -= amount
            print(f"Made a payment of {amount}")
        else:
            print("Insufficient cash")

    def get_supported_operations(self):
        return super().get_supported_operations() + ["Make Payment"]


atm1 = ATM(1000)
atm2 = OnlineATM(2000)

atms = [atm1, atm2]

for atm in atms:
    print(f"ATM Cash: {atm.cash}")
    print(f"Supported Operations: {atm.get_supported_operations()}")
    print("------------------------")
