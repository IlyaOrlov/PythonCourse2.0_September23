class Money:

    def __init__(self, rub, kop):
        self.rub = rub
        self.kop = kop

    def __str__(self):
        return f"{self.rub},{self.kop:02d}"

    def __add__(self, other):
        total_rub = self.rub + other.rub
        total_kop = self.kop + other.kop
        if total_kop >= 100:
            total_rub += total_kop // 100
            total_kop %= 100
        return Money(total_rub, total_kop)

    def __sub__(self, other):
        total_rub = self.rub - other.rub
        total_kop = self.kop - other.kop
        if total_kop < 0:
            total_rub -= 1
            total_kop += 100
        return Money(total_rub, total_kop)

    def __eq__(self, other):
        return (self.rub, self.kop) == (other.rub, other.kop)

    def __lt__(self, other):
        return (self.rub, self.kop) < (other.rub, other.kop)

    def __gt__(self, other):
        return (self.rub, self.kop) > (other.rub, other.kop)


res1 = Money(10, 11)
res2 = Money(5, 11)

res_sum = res1 + res2
print(f"Сумма: {res_sum}")
res_diff = res1 - res2
print(f"Вычитание: {res_diff}")
print(res1 > res2)
print(res1 < res2)
print(res1 == res2)
