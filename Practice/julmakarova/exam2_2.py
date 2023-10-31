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
        sum_n = float(self) + float(other)
        return Money(round(sum_n, 2))

    def __sub__(self, other):
        sub_n = float(self) - float(other)
        return Money(round(sub_n, 2))

    def __gt__(self, other):
        return float(self) > float(other)

    def __lt__(self, other):
        return float(self) < float(other)

    def __eq__(self, other):
        return float(self) == float(other)


m1 = Money(20, 90)
m2 = Money(29, 0)
print(m1)
print(m2)
print(m1 + m2)
print(m1 - m2)
print(m1 < m2)
