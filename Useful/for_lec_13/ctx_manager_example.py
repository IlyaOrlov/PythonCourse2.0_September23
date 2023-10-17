

class MyCtxManager:
    def __enter__(self):
        print("Входим в менеджер контекста")


    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Выходим из менеджера контекста")



with MyCtxManager():
    print(10 / 0)
