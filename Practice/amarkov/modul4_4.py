a = ("Ты сам-то понял, что написал?", "Аргументируй", "И?") # это кортеж с ответами компъютера


for i in a:
    print(i)

b = input("что - то понял, что - то нет: ")

while b != "хватит":
        print(a[0])

a = [0]
a += 1
print(a):