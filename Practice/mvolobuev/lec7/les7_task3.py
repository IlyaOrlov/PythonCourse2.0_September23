# Реализовать систему, эмулирующую работу с банкоматами.
# Создать семейство классов банкоматов, хранящих определенные суммы и поддерживающих различные операции
# (одни банкоматы принимают и выдают наличные, другие позволяют еще и проводить онлайн платежи).
# Операции реализуются посредством методов, выводящих название операции и меняющих (при необходимости)
# количество наличных в банкомате. Для тестирования системы необходимо реализовать алгоритм,
# обходящий список банкоматов разного типа и запрашивающий у каждого банкомата информацию о количестве наличных
# и наборе поддерживаемых операций.
class Banks:
    def __init__(self, address, deposit1, deposit2):
        self.address = address
        self.deposit1 = deposit1
        self.deposit2 = deposit2
        self.history = []
# Пополнение счета
    def vznos(self, i1):
        self.deposit1 += i1

    def snytie(self):
        print(f"На Вашем счету {atm.deposit1}")
        while True:
            j = int(input("Введите сумму которую хотите снять:"))
            if j < 0 or j > atm.deposit1:
                break
            else:
                self.deposit1 = self.deposit1 - j
                print(f"На Вашем счету осталось: {atm.deposit1}")
                return

    def batm(self):
        while True:
            jatm = int(input("Введите, банкомат с которым Вы хотите работать:  "))
            if jatm > 3:
                break
            else:
                return jatm - 1

class Atm_ilyinka(Banks):

# Снятие со счета
    def snytie(self):
        print(f"На Вашем счету {atm.deposit1}")
        while True:
            j = int(input("Введите сумму которую хотите снять:"))
            if j < 0 or j > atm.deposit1:
                break
            else:
                self.deposit1 = self.deposit1 - j
                print(f"На Вашем счету осталось: {atm.deposit1}")
                return

    def name(self):
        print("Банкомат установлен на улице Ильинская")
        print("<Вставьте карту")
        print("<Банкомат осуществляет операции по снятию со счета")
        io = 0
        return io


class Atm_vaneeva(Banks):
# Снятие со счета
    def snytie(self):
        print(f"На Вашем счету {atm.deposit1}")
        while True:
            j = int(input("Введите сумму которую хотите снять:"))
            if j < 0 or j > atm.deposit1:
                break
            else:
                self.deposit1 = self.deposit1 - j
                print(f"На Вашем счету осталось: {atm.deposit1}")
                return

    def name(self):
        print("Банкомат установлен на улице Ванеева")
        print("<Вставьте карту")
        print("<Банкомат осуществляет операции по снятию и пополнению счета")
        while True:
            io = int(input(" Для пополнения счета введите - 0, для снятия со счета - 1 :  "))
            if io > 1:
                break
            else:
                return io

# Пополнение счета
    def popolnenie(self):
        print(f"На Вашем счету {atm.deposit1}")
        while True:
            j = int(input("Введите сумму которую хотите положить на счет:"))
            if j < 0:
                break
            else:
                self.deposit1 = self.deposit1 + j
                print(f"На Вашем счету: {atm.deposit1}")
                return

class Atm_pokrovka(Banks):

# Снятие со счета
    def snytie(self):
        print(f"На Вашем счету {atm.deposit1}")
        while True:
            j = int(input("Введите сумму которую хотите снять:"))
            if j < 0 or j > atm.deposit1:
                break
            else:
                self.deposit1 = self.deposit1 - j
                print(f"На Вашем счету осталось: {atm.deposit1}")
                return

# Пополнение счета
    def popolnenie(self):
        print(f"На Вашем счету {atm.deposit1}")
        while True:
            j = int(input("Введите сумму которую хотите положить на счет:"))
            if j < 0:
                break
            else:
                self.deposit1 = self.deposit1 + j
                print(f"На Вашем счету: {atm.deposit1}")
                return

# Оплата квитанции
    def slip(self):
        print(f"На Вашем счету {atm.deposit2}")
        while True:
            j = int(input("Введите сумму с квитанции, которую хотите оплатить:"))
            if j < 0:
                break
            else:
                self.deposit2 = self.deposit2 - j
                print(f"На Вашем счету: {atm.deposit2}")
                return

    def name(self):
        print("Банкомат установлен на улице Покровская")
        print("<Вставьте карту")
        print("<Банкомат осуществляет операции по снятию, пополнению счета и оплаты квитанций")
        while True:
            io = int(input(" Для пополнения счета введите - 0, для снятия со счета - 1, для оплаты квитанции - 2 :  "))
            if io > 2:
                break
            else:
                return io

lst =[Atm_ilyinka("Ильинская", 1000, 0), Atm_vaneeva("Ванеева", 1000, 0), Atm_pokrovka("Покровская", 1000, 900)]
for i in range(0, len(lst)):
    print(f"Банкомат -{i+1} на ул. {lst[i].address}, снятие наличных / Депозит-1 {lst[i].deposit1} / Депозит-2 {lst[i].deposit2} ")
jatm = Banks.batm(lst)
#atm = lst[jatm]
atm = lst[jatm]
iu = atm.name()
if iu == 0:
    j1 = atm.snytie()
elif iu == 1:
    j1 = atm.popolnenie()
else:
        j1 = atm.slip()
