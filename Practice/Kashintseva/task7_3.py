class Bank:
    def __init__(self, sum, oper):
        self._sum = sum
        self._oper = oper

    def plus_money(self):
        self._sum += sum_plus

    def minus_money(self):
        self._sum -= sum_minus

    def pay(self):
        pass

    def info(self):
        print(f" {self._sum} наличных денег, поддерживает операции: {self._oper}")


class Bankomat(Bank):
    def __init__(self, sum, oper):
        super().__init__(sum, oper)

    def pay(self):
        self._sum -= sum_pay


b1 = Bankomat(100000, "Пополнение и снятие наличных")
b2 = Bankomat(200000, "Пополнение и снятие наличных")
b3 = Bankomat(300000, "Пополнение и снятие наличных, проведение онлайн-платежей")
choice = input(f"Выберите банкомат b1, b2 или b3: ")
if choice == "b1":
    op = input(f"Выберите операцию 1 (пополнить) или 2 (снять наличные): ")
    if op == "1":
        sum_plus = int(input(f"Введите сумму пополнения: "))
        b1.plus_money()
    elif op == "2":
        sum_minus = int(input(f"Введите сумму снятия: "))
        b1.minus_money()
    else:
        print("Ошибка ввода!")
elif choice == "b2":
    op = input(f"Выберите операцию 1 (пополнить) или 2 (снять наличные): ")
    if op == "1":
        sum_plus = int(input(f"Введите сумму пополнения: "))
        b2.plus_money()
    elif op == "2":
        sum_minus = int(input(f"Введите сумму снятия: "))
        b2.minus_money()
    else:
        print("Ошибка ввода!")
elif choice == "b3":
    op = input(f"Выберите операцию 1 (пополнить), 2 (снять наличные) или 3 (провести онлайн-платеж): ")
    if op == "1":
        sum_plus = int(input(f"Введите сумму пополнения: "))
        b3.plus_money()
    elif op == "2":
        sum_minus = int(input(f"Введите сумму снятия: "))
        b3.minus_money()
    elif op == "3":
        sum_pay = int(input(f"Введите сумму платежа: "))
        b3.pay()
    else:
        print("Ошибка ввода!")
lst = [b1, b2, b3]
for i, bank in enumerate(lst):
    print(f"Банкомат {i}: ")
    bank.info()
