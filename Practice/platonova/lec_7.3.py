class Bankomat:
    def __init__(self, name, summa):
        self.name = name
        self._summa = summa

    def plus_money(self):
        sum_plus = int(input(f"Пополнить баланс: "))
        self._summa += sum_plus

    def minus_money(self):
        sum_minus = int(input(f"Снять деньги: "))
        if self._summa > sum_minus:
            self._summa -= sum_minus
        else:
            print("В банкомате не достаточно денег.")

    def operat(self):
        oper = [b.plus_money, b.minus_money]
        return oper

    def info(self):
        print(f"В банкомате № {self.name}, его баланс составляет {self._summa},")

    @staticmethod
    def inf_oper():
        print("поддерживает операции: пополнение и снятие наличных.")


class Bankomat_online(Bankomat):
    @staticmethod
    def online_pay():
        sum_pay = int(input(f"Введите сумму платежа: "))
        print(f"Онлайн платеж на сумму {sum_pay} проведен")

    def operat(self):
        oper = [b.plus_money, b.minus_money, b.online_pay]
        return oper

    @staticmethod
    def inf_oper():
        print("поддерживает операции: пополнение, снятие, проведение онлайн платежей.")


b1 = Bankomat(1, 100)
b2 = Bankomat_online(2, 300)
lst = [b1, b2]
test = input(f"Выберите банкомат {[i for i, _ in enumerate(lst, 1)]}: ")
b = lst[int(test) - 1]
ops = b.operat()
i = input(f"Выберите операцию {[i for i, _ in enumerate(ops , 1)]}: ")
ops[int(i) - 1]()
for b in lst:
    b.info()
    b.inf_oper()