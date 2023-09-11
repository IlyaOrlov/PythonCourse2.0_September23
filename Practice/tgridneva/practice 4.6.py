def num(a, b):
    if a > b:
        _max = a
        print(a)
    elif b > a:
        _max = b
        print(b)


def num2(a, b):
    if a > b:
        _max = a
    elif b > a:
        _max = b
        return a


if __name__ == '__main__':
    num(a=2, b=3)
