def sred_arif_fun(array):
    summa = 0
    kol = 0
    for elem in array:
        if elem.isdecimal():
            x = int(elem)
            summa += x
            kol += 1
    res = summa / kol if kol != 0 else None
    return res


if __name__ == "__main__":
    # lst = []
    # while (user := input("Введите данные: ")) != "stop":
    #     lst.append(user)
    # print(lst)
    #
    # sa = sred_arif_fun(lst)
    # print(f"Среднее арифметическое: {sa}")

    r = sred_arif_fun(["300", "400", "abc"])
    print(f"{r=}")
    r = sred_arif_fun(["128", "e", "abc"])
    print(f"{r=}")
    r = sred_arif_fun([])
    print(f"{r=}")
