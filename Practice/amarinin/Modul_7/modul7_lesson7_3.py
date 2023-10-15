from abc import ABC, abstractmethod


class BankA(ABC):

    def __init__(self, name="БанкА", golds=1000000):
        self._name = name
        self._golds = golds

    def gold_in(self):
        gold = verification_gold(input(f"{self.gold_in.__name__}  <--  Давай! : "))
        print(f"{self.gold_in.__name__}  {gold}")
        self._golds = self._golds + gold

    def gold_out(self):
        gold = verification_gold(input(f"{self.gold_out.__name__}  -->  Сколько? : "))
        print(f"{self.gold_out.__name__}  {gold}")
        self._golds = (self._golds - gold) if gold < self._golds else print("Слишком много хочещь")

    def gold_online(self):
        gold = verification_gold(input(f"{self.gold_online.__name__}  <--  Давай? : "))
        print(f"{self.gold_online.__name__}  {gold}")
        self._golds = self._golds + gold

    @abstractmethod
    def info(self):
        print(self._name, self._golds)


class InGold(BankA):
    __slots__ = ()

    def gold_out(self):
        print(f"Non {super().gold_out.__name__}")

    def gold_online(self):
        print(f"Non {super().gold_online.__name__}")

    def info(self):
        return f"{self._name}  {self._golds} $ {self.gold_in.__name__}"


class OutGold(BankA):
    __slots__ = ()

    def gold_in(self):
        print(f"Non {super().gold_in.__name__}")

    def gold_online(self):
        print(f"Non {super().gold_online.__name__}")

    def info(self):
        return f"{self._name}  {self._golds} $ {self.gold_out.__name__}"


class InOutGold(BankA):
    __slots__ = ()

    def gold_online(self):
        print(f"Non {super().gold_online.__name__}")

    def info(self):
        return f"{self._name}  {self._golds} $ {self.gold_in.__name__}  {self.gold_out.__name__}"


class Online(BankA):
    __slots__ = ()

    def info(self):
        return (f"{self._name}  {self._golds} $ {self.gold_out.__name__}"
                f"  {self.gold_in.__name__}  {self.gold_online.__name__}")


def verification_gold(ins):
    return int(ins) if ins.isdecimal() else 0


if __name__ == "__main__":
    print([{i().info()} for i in BankA.__subclasses__()])

    auto1 = InGold()
    auto1.gold_in()
    print(auto1.info())
    auto2 = OutGold()
    auto2.gold_out()
    print(auto2.info())
    auto3 = InOutGold()
    auto3.gold_in()
    auto3.gold_out()
    print(auto3.info())
    auto4 = Online()
    auto4.gold_in()
    auto4.gold_out()
    auto4.gold_online()
    print(auto4.info())

    lst = (auto1, auto2, auto3, auto4)
    print([{i.info()} for i in lst])
