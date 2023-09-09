# программа, проверяющая, что слово, введённое пользователем, является палиндромом

slovoA = input("Введите слово: ")
slovoA = slovoA.lower()
slovoB = slovoA[::-1]
print(slovoA == slovoB)
