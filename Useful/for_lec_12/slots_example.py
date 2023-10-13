class Employee:
    __slots__ = ("_name", "_surname")

    def __init__(self):
        self._name = "Иван"
        self._surname = "Иванов"


emp = Employee()
