class Tank:
    def __init__(self, power, speed, x):
        self._power = power
        self._speed = speed
        self._x = x

    def move(self, i):
        self._x += self._speed * i

    def print(self):
        print(f"Это танк {type(self).__name__}, x = {self._x}")

    def shoot(self):
        pass


class T34(Tank):
    def shoot(self):
        print("Ba-bah")


class Tiger(Tank):
    def shoot(self):
        print("Bdysh-bdysh")


class IS(Tank):
    def shoot(self):
        print("Badoom")


lst = [T34(100, 30, 0), Tiger(150, 20, -1), IS(150, 20, 0)]
while True:
    print("В игре доступны следующие танки:")
    for i, tank in enumerate(lst):
        print(f"Танк {i}: ")
        tank.print()

    choice = int(input("Выберите танк (от 0 до 2): "))
    if choice > 2:
        break

    t = lst[choice]
    t.print()
    time_to_move = int(input("Введите время: "))
    t.move(time_to_move)
    t.shoot()
    t.print()

