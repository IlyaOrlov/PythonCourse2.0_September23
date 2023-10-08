# Задание 1. Класс и экземпляры классов
class Tank_Vybor:
    def __init__(self, marka, cvet, ckorost):
        self.marka = marka
        self.cvet = cvet
        self.ckorost = ckorost


w = Tank_Vybor
w.marka = "T-34"
w.cvet = "Зеленый"
w.ckorost = "50 км/ч"
print(w.marka)
print(w.cvet)
print(w.ckorost)
print("************************************")
w1 = Tank_Vybor
w1.marka = "T-80"
w1.cvet = "Песочный"
w1.ckorost = "80 км/ч"
print(w1.marka)
print(w1.cvet)
print(w1.ckorost)
