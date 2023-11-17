def anuta_format(f_str, *args, **kwargs):
    res = f_str

    if res.count("{") != len(args) + len(kwargs):
        print("Ошибка.Попробуйте еще раз ")
    else:
        for i in args:
            res = res.replace("{}", str(i), 1)
        for i, v in enumerate(args):
            res = res.replace("{" + str(i) + "}", str(v), 1)
        for k, v in kwargs.items():
            res = res.replace("{" + k + "}", str(v), 1)
    print(res)


if __name__ == "__main__":
    anuta_format("Сумма: {} + {} = {}", 5, 3, 5 + 3)

    s = "Сумма: {} + {} = {a}"
    anuta_format(s, 7, 3, a=7 + 3)

    s = "Сумма: {1} + {0} = {2}"
    anuta_format(s, 2, 7, 2 + 7)
