def povt(s):
    for i, n in enumerate(s):
        if s.index(n) != i:
            return n
    print("Цифры не повторяются!")


s1 = [7, 5, 8, 0, 50, 8, 2, 9, 2, 15, 0, -1]
print(f"Первый повторяющийся символ в списке: {povt(s1)}!")
