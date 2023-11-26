def input_vvod(z1, z2):
    if z1 > z2:
        return z1
    else:
        return z2

def print_vivod(maxi):
    print(f"Наибольшее число: {maxi}")


def print_viv(z1, z2):
    if z1 > z2:
        print(f"Наибольшее число: {z1}")
    else:
        print(f"Наибольшее число: {z2}")


print("Программа для определения наибольшего числа из двух введеных")
z1 = input("Введите первое число:   ")
z2 = input("Введите второе число:   ")
dx = input_vvod(z1, z2)
print_vivod(dx)
print_viv(z1, z2)