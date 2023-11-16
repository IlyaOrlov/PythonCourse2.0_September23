def fun(a, b, s):
    s(a, b)
    print(a + b)


def mock_print(res):
    assert res == 30


def mock_s(x, y):
    pass


bkp_print = print
print = mock_print
fun(10, 20, mock_s)
print = bkp_print


