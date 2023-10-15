class SSSRTanks:

    def __init__(self, model, ttype, max_speed):
        print("Теперь у вас есть танк!")
        self.model = model
        self.ttype = ttype
        self.max_speed = max_speed

    def print_info(self):
        print(f"Поздравляем! Вы выбрали танк: {self.model}, тип: {self.ttype}")

    def print_move(self):
        print(f"Максимальная скорость перемещения: {self.max_speed}")


e = SSSRTanks("Т-34", "лёгкий", 70)
e.print_info()
e.print_move()
e2 = SSSRTanks("КВ", "тяжёлый", 34)
e2.print_info()
e2.print_move()
