import os
import time
from multiprocessing import Pool


def add_all(d):
    time.sleep(0.1)
    print(f"N:{os.getpid() : < 8}{d[0] + d[1]}") if str(type(d[0])) == str(type(d[1])) \
        else print(os.getpid(), None)


if __name__ == "__main__":
    data = (5, 5), ("5", "5"), ([5], ['5'])
    pool = Pool(processes=4)
    pool.map(add_all, data)
