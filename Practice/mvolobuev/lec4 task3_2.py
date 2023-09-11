def bukv(b, alfa):
    nom = input(f"Введите порядковый номер для буквы: {b:}   : ")
    if nom.isdigit():
        nom = int(nom)
        mon = alfavit[nom - 1]
        bo1 = str(mon[1])
        if b == bo1:
            print(f"Цифра соответствует букве :                               {bo1:}")
            return
        else:
            print(f"Цифра соответствует букве                      {bo1:} 'попробйте еще раз")
            bukv(b, alfa)
    else:
        print("Вместо цифры введена буква :")
        bukv(b, alfa)


alfavit = [(1, "a"), (2,"b"),(3, "c"),(4, "d"),(5, "e"),(6, "f"),(7, "g"),(8, "h"),(9, "i"),(10, "j"),(11, "k"),
           (12,"l"),(13,"m"),(14, "n"),(15, "o"),(16, "p"),(17, "q"),(18, "r"),(19, "s"),(20, "t"),
           (21,"u"),(22, "v"),(23, "w"),(24, "x"),(25, "y"),(26, "z")]
print("Сегодня мы стараемся запомнить порядковый номер букв в алфавите, и набрать слово (stop)")
bs = alfavit[18]
bt = alfavit[19]
bo = alfavit[14]
bp = alfavit[15]
for k in range(0, 4):
    if k == 0:
        b = str(bs[1])
        bukv(b, alfavit)
    else:
        if k == 1:
            b = str(bt[1])
            bukv(b, alfavit)
        else:
            if k == 2:
                b = str(bo[1])
                bukv(b, alfavit)
            else:
                b = str(bp[1])
                bukv(b, alfavit)
print("Поздравляем, Вы ввели слово -stop-, цифры - 19-20-15-16")