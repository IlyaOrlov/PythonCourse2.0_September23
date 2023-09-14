def my_decorator(res):
    def wrapper():
        print("===========")
        res()
        print("===========")
        return res
    return wrapper


@my_decorator
def secret():
    print("Вроде работает")


secret()
