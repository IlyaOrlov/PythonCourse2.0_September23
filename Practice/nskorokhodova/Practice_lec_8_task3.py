class Bankomat(object):
    def __init__(self, amount):
        self.__amount = amount

    @property
    def amount(self):
        return self.__amount


def cashwithdrawal(self, nal):
    if nal <= self.__amount:
        self.__amount -= nal
        return print(f"На карте: {self.amount}")
    else:
        return print("Недостаточно средств.")


def deposit(self, nal):
    new_balance = self.amount + nal
    if new_balance > 0:
        self.__amount = new_balance
        return print(f"Остаток средств: {self.amount}")
    else:
        return print("Ошибка!")


class Online(Bankomat):
    def online_pay(self, amount):
        return print(f"Выполнен онлайн платеж на сумму: {amount}")

    def info(self):
        return "вывод/внесение средств и онлайн платежи"


bankomat1 = Bankomat(50)
bankomat2 = Online(100)
print(bankomat1.amount, bankomat2.amount)
