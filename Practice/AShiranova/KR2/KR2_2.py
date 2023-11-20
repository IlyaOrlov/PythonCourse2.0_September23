class NegativeMoneyError(Exception):
    pass


class StringFloatMoneyError(Exception):
    pass


class ValueMoneyError(Exception):
    pass


class Money:
    def __init__(self, rub, kop):
        if not isinstance(rub, int) or not isinstance(kop, int):
            raise StringFloatMoneyError("Извините. Можно ввести только целую сумму.")
        if rub < 0 or kop < 0:
            raise NegativeMoneyError("Ошибка. Вы ввели не корректную сумму..")
        if kop > 100:
            raise ValueMoneyError("Ошибка. Количество копеек не должно превышать 100")
        self.rub = rub
        self.kop = kop
        self.sum_many_kop = self.rub * 100 + self.kop

    def __str__(self):
        rub_str = str(self.rub)
        kop_str = str(self.kop) if self.kop > 9 else "0" + str(self.kop)
        return f"{rub_str},{kop_str}"

    def __add__(self, other):
        rub = (self.sum_many_kop + other.sum_many_kop) // 100
        kop = (self.sum_many_kop + other.sum_many_kop) % 100
        return Money(rub, kop)

    def __sub__(self, other):
        if self.sum_many_kop >= other.sum_many_kop:
            rub = (self.sum_many_kop - other.sum_many_kop) // 100
            kop = (self.sum_many_kop - other.sum_many_kop) % 100
            return Money(rub, kop)
        else:
            return None

    def __ne__(self, other):
        return self.sum_many_kop != other.sum_many_kop

    def __eq__(self, other):
        return self.sum_many_kop == other.sum_many_kop

    def __lt__(self, other):
        return self.sum_many_kop < other.sum_many_kop

    def __le__(self, other):
        return self.sum_many_kop <= other.sum_many_kop

    def __gt__(self, other):
        return self.sum_many_kop > other.sum_many_kop

    def __ge__(self, other):
        return self.sum_many_kop >= other.sum_many_kop


if __name__ == "__main__":

    m1 = Money(151, 50)
    m2 = Money(54, 13)
    m3 = Money(77, 25)
    m5 = m3 - m2
    print(f"sum: {m1} + {m2} = {m1 + m2}")
    print(f"sub: {m1} - {m2} = {m1 - m2}")
    print(f"sub: {m1} - {m3} = {m1 - m3}")
    print(f"Money : {m5}")
    print(m1 != m2)
    try:
        m6 = Money(-1, 1)
    except Exception as exc:
        print(exc)
