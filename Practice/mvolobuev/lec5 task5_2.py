# Замена проберов на Tab
s1 = ""
s2 = ""
slist = ""
with open("Piton.txt", "r", encoding="utf-8") as f1:
    for s in f1:
        s1 = " " + s.strip()
        s3 = s1.replace(" ", "\t", 1)
        slist = slist + s2 + s3
        s2= "\n"
        print(slist)

with open("Piton.txt","w",encoding= "utf-8") as f:
    f.write(slist)
