def one(square):
    def two(*args, **kwargs):
        print("===========")
        con = square(*args, **kwargs)
        print(con)
        print("===========")
        return con

    return two


@one
def square_tr(a, h):
    con = 0.5 * a * h
    return con


con = square_tr(20, 5)
