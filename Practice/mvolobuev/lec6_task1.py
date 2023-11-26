# Задание 1. Класс и экземпляры классов
class Tank_Vybor:
    def __init__(self, marka, cvet, ckorost):
        self.marka = marka
        self.cvet = cvet
        self.ckorost = ckorost


w = Tank_Vybor("T-34", "Зеленый", "50 км/ч")
print(w.marka)
print(w.cvet)
print(w.ckorost)
print("************************************")
w1 = Tank_Vybor("T-80", "Песочный", "80 км/ч")
print(w1.marka)
print(w1.cvet)
print(w1.ckorost)
