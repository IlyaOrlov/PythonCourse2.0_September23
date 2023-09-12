def telo_dekor(a,b,c):
    def podch(a,b,c):
        print("================")
        rex= fun_print(a,b,c)
        print("================")
        return rex
    return podch (a,b,c)


def fun_print(a,b,c):
    print(f"{a} + {b} = {c}")


def fun_sum(zn, zk):
    zl = zn + zk
    return zl


z1 = int(input("Введите первое число:   "))
z2 = int(input("Введите второе число:   "))
z = fun_sum(z1, z2)
telo_dekor(z1, z2, z)
