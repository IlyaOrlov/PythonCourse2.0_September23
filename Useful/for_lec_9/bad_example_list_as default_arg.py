def find_non_decimal(lst):
    for x in lst:
        if type(x) != int:
            return x
    return None


# Антипример: значение по умолчанию не должно быть изменяемого типа
def replace_non_decimal(lst=[""]):
    for i, x in enumerate(lst):
        if type(x) != int:
            lst[i] = None
    return lst

res = replace_non_decimal()
print(res)
res.append(100)

res1 = replace_non_decimal()
print(res1)
