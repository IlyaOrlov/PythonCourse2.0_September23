# Это быстрый пример для демонстрации возможностей менеджера контекста.
# Не используйте обращение к глобальным переменным в реальном коде.
def fun(x, y):
    print(x + y)


def fake_print(arg):
    global result
    result = arg


class MyCtxManager:
    def __enter__(self):
        global print
        self.bkp_print = print
        print = fake_print

    def __exit__(self, exc_type, exc_val, exc_tb):
        global print
        print = self.bkp_print


with MyCtxManager():
    fun(10, 20)

print(result == 30)
