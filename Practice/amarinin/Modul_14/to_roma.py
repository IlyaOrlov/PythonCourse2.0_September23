class NonValidInput(Exception):
    pass


def to_roman(num):
    if not num.isdecimal():
        raise NonValidInput("Должно быть число")
    num = int(num)
    if num > 5000 or num < 1:
        raise NonValidInput("Должно быть 1 - 5000")
    num_dict = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC',
                50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}
    res = ""
    for val, num_roma in num_dict.items():
        while num >= val:
            res += num_roma
            num -= val
    return res


if __name__ == "__main__":
    while True:
        try:
            num_str = input("Введите число: ")
            if num_str == "":
                break
            print(to_roman(num_str))
        except NonValidInput as e:
            print(e)
