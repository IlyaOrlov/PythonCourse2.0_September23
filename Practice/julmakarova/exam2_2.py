class Money:
    def __init__(self, *args):
        if len(args) == 2:
            self._rub = args[0]
            self._kop = args[1]
        else:
            s = f'{args[0]}'
            lst = s.split('.')
            self._rub = lst[0]
            self._kop = lst[1]

    def __str__(self):
        return f"{self._rub},{self._kop}"

    def __float__(self):
        st = f'{self._rub}.{self._kop}'
        fl = float(st)
        return fl

    def __add__(self, other):
        # sum_kop = self._kop + other._kop
        # i = 0
        # if sum_kop >= 100:
        #     i = sum_kop//100
        #     sum_kop = sum_kop%100
        # sum_rub = self._rub + other._rub + i
        # s = Money(sum_rub, sum_kop)
        # return s
        sum_n = float(self) + float(other)
        return Money(round(sum_n, 2))

    def __sub__(self, other):
        # sub_rub = self._rub - other._rub
        # sub_kop = self._kop - other._kop
        # if sub_kop < 0:
        #     if sub_rub > 0:
        #         sub_kop += 100
        #         sub_rub -= 1
        #     elif sub_rub < 0:
        #         sub_kop *= -1
        #     else:
        #         sub_kop *= -1
        #         sub_rub *= -1
        # s = Money(sub_rub, sub_kop)
        # return s
        sub_n = float(self) - float(other)
        return Money(round(sub_n, 2))

    def __gt__(self, other):
        # if self._rub > other._rub or self._rub == other._rub and self._kop > other._kop:
        #     return True
        # return False
        return float(self) > float(other)

    def __lt__(self, other):
        # if self._rub < other._rub or self._rub == other._rub and self._kop < other._kop:
        #     return True
        # return False
        return float(self) < float(other)

    def __eq__(self, other):
        # if self._rub == other._rub and self._kop == other._kop:
        #     return True
        # return False
        return float(self) == float(other)


m1 = Money(20, 90)
m2 = Money(29, 0)
print(m1)
print(m2)
print(m1 + m2)
print(m1 - m2)
print(m1 < m2)
