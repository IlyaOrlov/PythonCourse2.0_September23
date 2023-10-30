class NegativeMoneyError(Exception):
    pass


class StringFloatMoneyError(Exception):
    pass


class ValueMoneyError(Exception):
    pass


class Money:
    def __init__(self, rub, kop):
        try:
            if isinstance(rub, str | float) or isinstance(kop, str | float):
                raise StringFloatMoneyError("Извините. Допустим только ввод целых положительных чисел")
            if rub < 0 or kop < 0:
                raise NegativeMoneyError("Извините. Ввод отрицательных значений не допустим")
            if kop > 100:
                raise ValueMoneyError("Извините. Количество копеек не должно превышать 100")
            self.rub = rub
            self.kop = kop
            self.sum_many_kop = self.rub * 100 + self.kop
        except StringFloatMoneyError as exc:
            print(exc)
            return
        except NegativeMoneyError as exc:
            print(exc)
            return
        except ValueMoneyError as exc:
            print(exc)
            return

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
    m1 = Money(1, 5)
    m2 = Money(1, 4)
    m3 = Money(20, 13)
    m5 = m3 - m2
    print(f"sum: {m1} + {m2} = {m1 + m2}")
    print(f"sub: {m1} - {m2} = {m1 - m2}")
    print(f"sub: {m1} - {m3} = {m1 - m3}")
    print(f"Money : {m5}")
    print(m1 != m2)
    m6 = Money(-1, 1)
