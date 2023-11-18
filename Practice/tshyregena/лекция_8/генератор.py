with open("для_итератора.txt.", "r", encoding="utf-8") as file:
    def gen():
        for line in file:
            print(file.readline())
            yield line


    r = gen()
    for i in r:
        print(i)
    # print(next(r))
    # print(next(r))
    # print(next(r))







