def decorator(func):
    def wrapper(*args, **kwargs):
        print("===========")
        s = func(*args, **kwargs)
        print("===========")
        return s

    return wrapper


@decorator
def plus(a, b):
    print(a + b)


plus("begin", "end")
