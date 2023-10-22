class User:
    def __init__(self, name, surname):
        self._name = name
        self._surname = surname

    def show(self):
        print(f"I'm {self._name} {self._surname}")