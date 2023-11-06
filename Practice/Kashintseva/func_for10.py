def find_primes(start=3, end=None):
    if end is None:
        end = start
    lst = []
    for i in range(start, end+1):
        for x in range(2, i):
            if i % x == 0:
                break
        else:
            lst.append(i)
    return lst
