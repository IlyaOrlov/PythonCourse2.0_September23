class Bankomat:
    def __init__(self, name, max_balans, balans):
        self.name = name
        self._max_balans = max_balans
        self._balans = balans
        print(f"Создан {self.name}.  Остаток на начало дня {self._balans} руб.")

    @staticmethod
    def info():
        print("Здравствуйте! Данный банкомат поддерживает только операции выдачи и внесения наличных! ")

    @property
    def balans(self):
        if self._balans > 0:
            return self._balans
        else:
            print("По техническим причинам банкомат не работает!")

    @balans.setter
    def balans(self, new_balans):
        if isinstance(new_balans, int):
            self._balans = new_balans
        else:
            print("Ошибка!")

    def dispense(self, amount):  # Выдача
        if self._balans < amount:
            return f"{self.name} не может выдать {amount} руб. В банкомате недостаточно средств."
        else:
            self._balans -= amount
            print(f"{self.name}. Выдача {amount} руб.")

    # Метод внесения средств, проверка на переполнение
    def deposit(self, amount):
        if (self._balans + amount) > self._max_balans:
            print(f"Переполнение! {self.name} не может принять {amount} руб.")
            return
        self._balans += amount
        print(f"{self.name}. Внесение {amount} руб.")


class BankomatOnlain(Bankomat):

    @staticmethod
    def info():
        print("Здравствуйте! Данный банкомат поддерживает операции выдачи, внесения наличных, а так же онлайн-платёж! ")

    def payments(self, zapros):
        if isinstance(zapros, int):
            return f"Через {self.name} осуществлён онлайн-платёж на сумму {zapros} руб."
        else:
            print(f"Некорректный платёж")


if __name__ == "__main__":
    Bank1 = Bankomat('Первый банкомат', 5000, 1000)
    Bank2 = Bankomat('Второй банкомат', 10000, 4000)
    Bank3 = BankomatOnlain('Третий банкомат', 20000, 3000)
    Bank4 = BankomatOnlain('Четвёртый банкомат', 50000, 2000)
    bank = [Bank1, Bank2, Bank3, Bank4]
    for a in bank:
        print(f"\n{a.name}. Баланс на начало дня {a.balans} руб.")
        a.info()
        a.dispense(500)
        a.dispense(5000)
        a.deposit(400)
        a.deposit(5000)
        print(f"\n{a.name}. Остаток на конец дня {a.balans} руб.")
        print("===========================")
    print(Bank3.payments(400))
