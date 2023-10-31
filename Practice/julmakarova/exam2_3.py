import re


def my_format_str(s, *args):
    i = 0
    n = 0
    l3 = ""
    while i < len(s) - 1:
        if s[i] == "{":
            sym = s[i + 1]
            if sym.isdecimal():
                if int(sym) < len(args):
                    l3 += args[int(sym)]
                    i += 3
                else:
                    print("Допущена ошибка в количестве аргументов!")
                    return None
            elif sym == "}":
                if n < len(args):
                    l3 += args[n]
                    i += 2
                    n += 1
                else:
                    print("Допущена ошибка в количестве аргументов!")
                    return None
        else:
            l3 += s[i]
            i += 1
    return l3


def my_format_re(s, *args):
    pt = re.compile(r'{(.?)}')
    l1 = re.findall(pt, s)
    l2 = []
    for i, n in enumerate(l1):
        try:
            if n == "":
                l2.append(args[i])
            else:
                l2.append(args[int(n)])
        except IndexError:
            print("Ошибка в количестве аргументов!")
            return None

    for j in range(0, len(l2)):
        s = re.sub(pt, l2[j], s, 1)
    return s


def my_format_str1(s, *args):
    for i, j in enumerate(args):
        s = s.replace('{' + str(i) + '}', str(j), 1).replace('{}', str(j), 1)

    return s


def my_format_re1(s, *args):
    for i, j in enumerate(args):
        s = re.sub("{" + str(i) + "?}", j, s, 1)
    return s


print(my_format_str("{} + {} = {}", 'a', 'b', 'a+b', 'c'))
print(my_format_str1("{} + {} = {}", 'a', 'b', 'a+b', 'c'))
print(my_format_re("{2} + {0} = {1} ", 'a', 'b', 'a+b', 'c'))
print(my_format_re1("{} + {} = {} ", 'a', 'b', 'a+b', 'c'))
