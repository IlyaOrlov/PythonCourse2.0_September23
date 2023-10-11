class Bankomat:
    def __init__(self, summa):
        self._summa = summa

    def plus_money(self):
        self._summa += sum_plus

    def minus_money(self):
        if self._summa >= sum_minus:
            self._summa -= sum_minus
        else:
            print("В банкомате нет запрашиваемой суммы.")

    @staticmethod
    def operat():
        print("поддерживает операции: пополнение и снятие наличных.")

    def info(self):
        print(f" {self._summa} наличных денег,")


class Bankomatik(Bankomat):
    def online_pay(self):
        return self._summa

    @staticmethod
    def operat():
        print("поддерживает операции: пополнение, снятие наличных, проведение онлайн-платежей.")


b1 = Bankomat(100000)
b2 = Bankomat(200000)
b3 = Bankomatik(300000)
choice = input(f"Выберите банкомат 1, 2 или 3: ")
if choice == "1" or choice == "2":
    op = input(f"Выберите операцию 1 (пополнить) или 2 (снять наличные): ")
    if op == "1":
        sum_plus = int(input(f"Введите сумму пополнения: "))
        if choice == "1":
            b1.plus_money()
        else:
            b2.plus_money()
    elif op == "2":
        sum_minus = int(input(f"Введите сумму снятия: "))
        if choice == "1":
            b1.minus_money()
        else:
            b2.minus_money()
    else:
        print("Ошибка ввода!")
elif choice == "3":
    op = input(f"Выберите операцию 1 (пополнить), 2 (снять наличные) или 3 (провести онлайн-платеж): ")
    if op == "1":
        sum_plus = int(input(f"Введите сумму пополнения: "))
        b3.plus_money()
    elif op == "2":
        sum_minus = int(input(f"Введите сумму снятия: "))
        b3.minus_money()
    elif op == "3":
        sum_pay = int(input(f"Введите сумму платежа: "))
        b3.online_pay()
    else:
        print("Ошибка ввода!")
else:
    print("Некорректный выбор банкомата!")
lst = [b1, b2, b3]
for i, bank in enumerate(lst):
    print(f"Банкомат {i+1}: ")
    bank.info()
    bank.operat()
