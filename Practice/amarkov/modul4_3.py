a = "" # Строка, куда будем набирать символы.
sym = input("Введите символ:")
print(a.isdecimal())

while sym != "stop":
      a += sym
      sym = input("Введите символ:")
      print(a)
