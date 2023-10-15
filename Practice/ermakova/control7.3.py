class ATM:
    def __init__(self, cash):
        self._cash = cash

    @property
    def cash(self):
        if self._cash > 0:
            return self._cash
        else:
            return f"Денег нет"

    @staticmethod
    def info():
        return "Только операции по снятию и внесению наличных"

    def plus_cash(self, money):
        if isinstance(money, int):
            self._cash += money
            return f"Новый кеш {self.cash}"
        else:
            return "Ошибка. Вы внесли не деньги"

    def minus_cash(self, money):
        if isinstance(money, int):
            if money < self.cash:
                self._cash -= money
                return f"Новый кэш: {self.cash}"
            else:
                return "Ошибка. Столько денег нет"
        else:
            return "Ошибка. Вы внесли не деньги"

    def __str__(self):
        return f"{self.info()}. Иммет кэш: {self.cash}"


class Terminal(ATM):

    @staticmethod
    def info():
        return "Операции по снятию, внесению наличных, а также онлайн платежи"

    @staticmethod
    def pay(summa):
        if isinstance(summa, int):
            return f"Вы отправили платеж суммой {summa}"
        else:
            return "Вы ввели некорректный платеж"


b1 = ATM(10000)
b2 = ATM(80000)
t1 = Terminal(5000)
print(b1)
print(b2)
print(t1)
print(b1.plus_cash(20))
print(b2.minus_cash(5000))
print(t1.pay(10000))

lst = [b1, b2, t1]
for i in lst:
    print(i)
