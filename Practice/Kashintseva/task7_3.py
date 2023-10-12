class Bankomat:
    def __init__(self, summa):
        self._summa = summa

    def plus_money(self):
        sum_plus = int(input(f"Введите сумму пополнения: "))
        self._summa += sum_plus

    def minus_money(self):
        sum_minus = int(input(f"Введите сумму снятия: "))
        if self._summa >= sum_minus:
            self._summa -= sum_minus
        else:
            print("В банкомате нет запрашиваемой суммы.")

    def operat(self):
        oper = [b.plus_money, b.minus_money]
        return oper

    def info(self):
        print(f" {self._summa} наличных денег,")

    @staticmethod
    def inf_oper():
        print("поддерживает операции: пополнение и снятие наличных.")


class Bankomatik(Bankomat):
    @staticmethod
    def online_pay():
        sum_pay = int(input(f"Введите сумму платежа: "))
        print(f"Онлайн-платеж на сумму {sum_pay} проведен успешно!")

    def operat(self):
        oper = [b.plus_money, b.minus_money, b.online_pay]
        return oper

    @staticmethod
    def inf_oper():
        print("поддерживает операции: пополнение, снятие наличных, проведение онлайн-платежей.")


b1 = Bankomat(100000)
b2 = Bankomat(200000)
b3 = Bankomatik(300000)
lst = [b1, b2, b3]
choice = input(f"Выберите банкомат 1, 2 или 3: ")
b = lst[int(choice) - 1]
ops = b.operat()
i = input("Выберите операцию: ")
ops[int(i) - 1]()
print(f"Банкомат {i}: ")
b.info()
b.inf_oper()
