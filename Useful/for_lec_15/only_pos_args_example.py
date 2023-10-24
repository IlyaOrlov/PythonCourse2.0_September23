def mylen(obj, /):
    cnt = 0
    for _ in obj:
        cnt += 1
    return cnt


print(mylen([1, 2, 3 ,4]))
