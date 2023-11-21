class Bankomat:
    def __init__(self, name, max_balans, balans):
        self.name = name
        self._max_balans = max_balans
        self._balans = balans
        print(f"{self.name}: Остаток на начало дня {self._balans} руб.")

    @staticmethod
    def info():
        print("В данном банкомате реализуются ТОЛЬКО операции выдачи и внесения наличных!")

    @property
    def balans(self):
        if self._balans > 0:
            return self._balans
        else:
            print("Баланс исчерпан!")

    def dispense(self, amount):
        if self._balans < amount:
            print(f"В банкомате недостаточно средств.")
        else:
            self._balans -= amount
            print(f"{self.name}: Выдача {amount} руб.")

    def deposit(self, amount):
        if (self._balans + amount) > self._max_balans:
            print(f"Переполнение!")
        else:
            self._balans += amount
            print(f"{self.name}: Внесение {amount} руб.")


class BankomatOnlain(Bankomat):

    @staticmethod
    def info():
        print("Данный банкомат поддерживает операции выдачи, внесения наличных и онлайн-платежи!")

    def payments(self, zapros):
        if isinstance(zapros, int):
            return f"Через {self.name} осуществлён онлайн-платёж на сумму {zapros} руб."
        else:
            print(f"Некорректный платёж")


bank1 = Bankomat('Первый банкомат', 10000, 2000)
bank2 = BankomatOnlain('Второй банкомат', 20000, 9000)
bank = [bank1, bank2]
for a in bank:
    print(f"\n{a.name}: Баланс на начало дня {a.balans} руб.")
    a.info()
    a.dispense(5000)
    a.dispense(5000)
    a.dispense(500)
    a.deposit(400)
    a.deposit(5000)
    print(f"\n{a.name}: Остаток на конец дня {a.balans} руб.")
    print("===========================")
print(bank2.payments(400))
