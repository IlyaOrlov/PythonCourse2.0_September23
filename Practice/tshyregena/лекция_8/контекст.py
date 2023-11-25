import time


class MyMen:
    def __enter__(self):
        self.start_time = time.time()
        print("Входим в менеджер контекста")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Выходим из менеджера контекста")
        elapsed_time = time.time() - self.start_time
        print(f"Время выполнения операции: {elapsed_time}")


with MyMen() as timer:
    kidd = "Кошка мяукает. Собака лает. Птичка чирикает. Лягушка квакает."
    a = dict(мяукает='говорит - мяу', лает='говорит - гав', чирикает='говорит - чирик-чирик',
             квакает='говорит - ква-ква')
    for key, value in a.items():
        kidd = kidd.replace(key, value)
    print(kidd)
