def fun(t, filename, *args):
    n = None
    if t == "*":
        n = 1
        for i in args:
            n *= i
    elif t == "+":
        n = 0
        for i in args:
            n += i
    with open(filename, "w") as f:
        f.write(f"{n}")
