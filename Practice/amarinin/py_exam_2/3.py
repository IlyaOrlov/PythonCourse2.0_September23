def my_format(f_str, *args, **kwargs):
    res = f_str

    if res.count("{") != len(args) + len(kwargs):
        print("что то вы напутали ")
    else:
        for i in args:
            res = res.replace("{}", str(i), 1)
        for i, v in enumerate(args):
            res = res.replace("{" + str(i) + "}", str(v), 1)
        for k, v in kwargs.items():
            res = res.replace("{" + k + "}", str(v), 1)
    print(res)


if __name__ == "__main__":
    my_format("Сумма: {} + {} = {}", 5, 3, 5 + 3)

    s = "Сумма: {} + {} = {a}"
    my_format(s, 1, 2, a=1 + 2)

    s = "Сумма: {a} + {b} = {c}"
    my_format(s, a=10, b=20, c=10 + 20)

    s = "Сумма: {1} + {0} = {2}"
    my_format(s, 5, 3, 5 + 3)
