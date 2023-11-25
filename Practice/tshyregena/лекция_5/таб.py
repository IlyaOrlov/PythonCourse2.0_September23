with open("таб.txt", "r+", encoding="utf-8") as f:
    s = f.read()
    print(s)
    p = input("Свернуть или развернуть символы табуляции: ").lower()
    k = ""
    if p == "свернуть":
        k = s.replace('    ', '\t')
    else:
        k = s.replace('\t', ' ')
with open("таб.txt", "w") as f:
    f.write(k)
