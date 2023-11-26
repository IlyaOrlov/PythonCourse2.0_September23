# Замена проберов на Tab
s2 = "\n"
slist = ""
with open("Piton.txt", "r", encoding="utf-8") as f1:
    for s in f1:
        slist += s.replace("    ", "\t") + s2
        print(slist)

with open("Piton.txt","w",encoding= "utf-8") as f:
    f.write(slist)
