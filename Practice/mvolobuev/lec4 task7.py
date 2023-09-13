def telo_dekor(fun):
    def podch(*args, **kwargs):
        print("================")
        rex= fun(*args, **kwargs)
        print("================")
        return rex
    return podch


@telo_dekor
def fun_print(a,b,c):
    print(f"{a} + {b} = {c}")


def fun_sum(zn, zk):
    zl = zn + zk
    return zl


z1 = int(input("Введите первое число:   "))
z2 = int(input("Введите второе число:   "))
z = fun_sum(z1, z2)
fun_print(z1,z2,z)
#telo_dekor(z1, z2, z)
