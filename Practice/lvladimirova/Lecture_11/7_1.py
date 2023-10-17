class Man:
    def __init__(self, name):
        self._name = name

    @staticmethod
    def solve_task():
        print("I'm not ready yet")

    def show(self):
        print(f"{self._name}")


if __name__ == "__main__":
    people = Man("Иван")
    people.show()
    Man.solve_task()
