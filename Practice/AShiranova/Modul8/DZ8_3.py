class ATM:
    def __init__(self, cash):
        self._cash = cash

    @property
    def cash(self):
        if self._cash > 0:
            return self._cash
        else:
            return f"Отсутствуют наличные"

    @staticmethod
    def info():
        return "Доступны только операции по снятию и внесению наличных"

    def plus_cash(self, money):
        if isinstance(money, int):
            self._cash += money
            return f"Новый кеш {self.cash}"
        else:
            return "Ошибка. Купюры не распознаны"

    def minus_cash(self, money):
        if isinstance(money, int):
            if money < self.cash:
                self._cash -= money
                return f"Новый кэш: {self.cash}"
            else:
                return "Ошибка. Не достаточно средств"
        else:
            return "Ошибка. Купюры не распознаны"

    def __str__(self):
        return f"{self.info()}. Иммет кэш: {self.cash}"


class Terminal(ATM):

    @staticmethod
    def info():
        return "Операции по снятию, внесению наличных, а также онлайн платежи"

    @staticmethod
    def pay(summa):
        if isinstance(summa, int):
            return f"Платеж суммой {summa} - отправлен"
        else:
            return "Вы ввели не корректную сумму"


b1 = ATM(15000)
b2 = ATM(7000)
t1 = Terminal(7000)
print(b1)
print(b2)
print(t1)
print(b1.plus_cash(50))
print(b2.minus_cash(7000))
print(t1.pay(15000))

lst = [b1, b2, t1]
for i in lst:
    print(i)
