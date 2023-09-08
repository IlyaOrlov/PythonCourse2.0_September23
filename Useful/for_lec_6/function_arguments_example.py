def fun(a: int, b: int) -> int:
    print(f"{a=}, {b=}")
    return a + b


def fun2(a: str, b: str) -> str:
    print(f"{a=}, {b=}")
    return a + b


def superfun(*args):
    print(args)
    print(len(args))
    for i in args:
        print(i)


def superfun2(**kwargs):
    print(kwargs)
    print(len(kwargs))
    for i in kwargs:
        print(i)


def supermegafun(param, *args, **kwargs):
    print(f"{param=}")
    print(f"{args=}")
    print(f"{kwargs=}")


# superfun(10, 20, "abc", 7, "x")
# superfun2(a=10, b=20, c="abc", x=7, y="x")
supermegafun(700, 10, 20, "abc", 7, "x", a=10, b=20, c="abc", x=7, y="x")