def num(a, b):
    if a > b:
        print(a)
    else:
        print(b)


def num2(a, b):
    if a > b:
        return a
    else:
        return b


if __name__ == '__main__':
    num(a=2, b=3)
    result = num2(a=2, b=3)
    print(result)

