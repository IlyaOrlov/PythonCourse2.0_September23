class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Имя подключенного пользователя: {self.name}, возраст {self.age}"
