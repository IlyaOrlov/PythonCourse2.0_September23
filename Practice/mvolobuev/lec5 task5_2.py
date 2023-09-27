# Замена проберов на Tab
i = 0
slist = []
with open("Piton.txt", "r", encoding="utf-8") as f1:
    for s in f1:
        slist = "\t" + s.lstrip()
        i += 1
        print(slist)

with open("Piton.txt","w",encoding= "utf-8") as f:
    f.write(slist)