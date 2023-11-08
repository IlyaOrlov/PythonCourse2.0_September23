class Bankomat:
    ONLINE_PAYMENT = "Онлайн платежи"

    def __init__(self, balance):
        self.balance = balance
        self.supported_operations = []

    def check_balance(self):
        print(f"Баланс: {self.balance}")

    def deposit(self, amount):
        self.balance += amount
        print(f"Пополнение на сумму {amount} прошло успешно. Новый баланс: {self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Снятие наличных в размере {amount} прошло успешно. Новый баланс: {self.balance}")
        else:
            print("Недостаточно средств на счете.")

    def get_supported_operations(self):
        print(self.supported_operations)

    def make_online_payment(self, amount):
        pass


class Online(Bankomat):
    def __init__(self, balance):
        super().__init__(balance)
        self.supported_operations = [Bankomat.ONLINE_PAYMENT]

    def make_online_payment(self, amount):
        if Bankomat.ONLINE_PAYMENT in self.supported_operations:
            if self.balance >= amount:
                self.balance -= amount
                print(f"Онлайн платеж в размере {amount} прошел успешно. Новый баланс: {self.balance}")
            else:
                print("Недостаточно средств на счете.")
        else:
            print("Операция 'Онлайн платеж' не поддерживается этим банкоматом.")


atm1 = Bankomat(1000)
atm2 = Online(2000)

atms = [atm1, atm2]

for atm in atms:
    print(f"Банкомат с балансом  {atm.balance}")
    atm.check_balance()
    atm.get_supported_operations()

    atm.deposit(200)
    atm.withdraw(300)
    print("\n")
