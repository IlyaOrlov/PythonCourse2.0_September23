def desing(func):
    def wrapper(*args, **kwargs):
        print("===========")
        res = func(*args, **kwargs)
        print("===========")
        return res
    return wrapper


@desing
def number_max(a, b):
    print(f"{a if a > b else b}")


if __name__ == "__main__":
    number_max(1, 10)
