s = input("Введите слово: ")
s1 = s.replace("А", "*").replace("A", "*")  # Замены две поскольку стоит учитывать русскую и английскую раскладку
print(f"Слово с заменой выглядит следующим образом: {s1}")
