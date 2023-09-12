def input_vvod():
    z1 = input("Введите первое число:   ")
    z2 = input("Введите второе число:   ")
    if z1 > z2: return z1
    if z1 <= z2: return z2

def print_vivod(maxi):
    print(f"Наибольшее число: {maxi}")


print("Программа для определения наибольшего числа из двух введеных")
dx = input_vvod()
print_vivod(dx)
