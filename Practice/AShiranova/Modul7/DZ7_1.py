class Tanks:
    def __init__(self, name, kind, arms):
        self.name = name
        self.kind = kind
        self.arms = arms

    def info(self):
        print(f"Данные о танке: название техники - {self.name}, "
              f"классификация по массе - {self.kind}, вооружение - {self.arms}.")


t1 = Tanks("WZ-132A", "heavy", "Пулемет")
t2 = Tanks("T49", "light", " Пулемет + малокалиберная пушка")
t3 = Tanks("AMX", "medium", "Орудие крупного калибра + пулемёт")
t1.info()
t2.info()
t3.info()
