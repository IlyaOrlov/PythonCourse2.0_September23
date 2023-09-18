def my_decorator(res):
    def wrapper(*args, **kwargs):
        print("===========")
        result = res(*args, **kwargs)
        print("===========")
        return result
    return wrapper


@my_decorator
def secret():
    print("Вроде работает")


secret()
