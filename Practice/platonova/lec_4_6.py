def max_of_two(a, b):
    if a > b:
        return a
    else:
        return b


a = int(input("первое число: "))
b = int(input("второе число: "))
print(max_of_two(a, b))