def maxi_1(a, b):
    if a > b:
        print(f"Наибольшее число: {a=}")
    else:
        print(f"Наибольшее число: {b=}")

def maxi_2(a, b):
    if a > b:
        return a
    else:
        return b


a = input("Введите число а: ")
b = input("Введите число b: ")

maxi_1(a, b)
print(f"Большее число: {maxi_2(int(a), int(b))}")
