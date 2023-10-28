class MyMetaClass(type):
    # "Child", (Parent,), {"attr1": 200}
    def __new__(cls, *args, **kwargs):
        print(f"{args=}")
        d = args[2]
        lst = []
        for k in d.keys():
            if len(k) > 1 and k[0] == '_' and k[1] != '_':
                lst.append(k)
        print(f"{lst=}")
        for k in lst:
            d[f"_{args[0]}{k}"] = d[k]  # _MyClass_a
            del d[k]
        print(f"{d=}")
        return super().__new__(cls, *args, **kwargs)


class MyClass(metaclass=MyMetaClass):
    _a = 10
    _b = 45
    _c = 100
    b = 20


print(MyClass._MyClass_a)
