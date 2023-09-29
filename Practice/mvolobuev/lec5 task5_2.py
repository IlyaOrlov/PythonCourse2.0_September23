# Замена проберов на Tab
s2 = ""
with open("Piton.txt", "r", encoding="utf-8") as f1:
    for s in f1:
        s1 = " " + s.strip()
        slist = slist + s2 + s1.replace(" ", "\t", 1)
        s2= "\n"
        print(slist)

with open("Piton.txt","w",encoding= "utf-8") as f:
    f.write(slist)
