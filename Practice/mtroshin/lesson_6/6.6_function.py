def mini(a, b):
    if a < b:
        return a
    else:
        return b

def maxi(a, b):
    if a > b:
        return a
    else:
        return b


a = input("Введите число а: ")
b = input("Введите число b: ")

print(f"Меньшее число: {mini(int(a), int(b))}")
print(f"Большее число: {maxi(int(a), int(b))}")
