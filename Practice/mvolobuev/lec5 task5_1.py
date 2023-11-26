# Замена Tab на пробелы
h = int(input("Введите количество пробелов вместо Tab: "))
slist = []
with open("Piton.txt", "r", encoding="utf-8") as f1:
    for s in f1:
        slist.append(s.expandtabs(tabsize=h))
        print(slist)

with open("Piton.txt","w",encoding= "utf-8") as f:
    for i1 in range(0, len(slist)):
        f.write(slist[i1])
