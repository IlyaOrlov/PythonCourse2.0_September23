with open("таб.txt", "r", encoding="utf-8") as f:
    s = f.read()
    p = input("Свернуть или развернуть символы табуляции: ").lower()
    k = ""
    if p == "свернуть":
        k = s.replace('    ', '\t')
    else:
        print(s)
    print(k)
