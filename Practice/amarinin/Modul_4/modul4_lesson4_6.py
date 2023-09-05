def max_number_print(num1, num2):
    print(num1 if num1 > num2 else num2)


def max_number_return(num1, num2):
    return num1 if num1 > num2 else num2


if __name__ == "__main__":
    max_number_print(55.91, 55)
    max_numbers = max_number_return(-55.99, 0.555)
    print(max_numbers)
