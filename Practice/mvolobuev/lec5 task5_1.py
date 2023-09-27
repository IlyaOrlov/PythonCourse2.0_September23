# Замена Tab на пробелы
h = int(input("Введите количество пробелов вместо Tab: "))
i = 0
slist = []
with open("Piton.txt", "r", encoding="utf-8") as f1:
    for s in f1:
        slist.append(s.expandtabs(tabsize=h))
        i += 1
        print(slist)

with open("Piton.txt","w",encoding= "utf-8") as f:
    f.write(slist[i-1])
