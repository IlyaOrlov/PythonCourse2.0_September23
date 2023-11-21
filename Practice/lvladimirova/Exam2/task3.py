def frmt(strn, *args, **kwargs):
    for i, arg in enumerate(args):
        strn = strn.replace("{}", str(arg), 1)
    for x, y in kwargs.items():
        strn = strn.replace("{" + x + "}", str(y))
    print(strn)


if __name__ == "__main__":
    frmt("Сумма: {} + {} = {}", 5, 3, 5 + 3)

    s = "Сумма: {} + {} = {a}"
    frmt(s, 1, 2, a=1 + 2)

    s = "Сумма: {a} + {b} = {c}"
    frmt(s, a=10, b=20, c=10 + 20)
