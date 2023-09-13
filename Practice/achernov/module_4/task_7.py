def my_decorator(res):
    def wrapper():
        print("===========")
        res()
        print("===========")
    return wrapper


@my_decorator
def secret():
    print("Вроде работает")
