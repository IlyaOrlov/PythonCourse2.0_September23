# Замена проберов на Tab
i = 0
s2 = ""
with open("Piton.txt", "r", encoding="utf-8") as f1:
    slist = ""
    for s in f1:
        s1 = " " + s.strip()
        slist = slist + s2 + s1.replace(" ", "\t", 1)
        s2= "\n"
        i += 1
        print(slist)

with open("Piton.txt","w",encoding= "utf-8") as f:
    f.write(slist)
