import os
import time
from multiprocessing import Pool


def add_all(d):
    time.sleep(0.1)
    print(f"N:{os.getpid() : < 8}{d[0] + d[1]}") if (type(d[0])) == (type(d[1])) \
        else print(os.getpid(), None)


if __name__ == "__main__":
    data = [(5, 5), ("5", "5"), ([5], ['5'])]
    with Pool(processes=4) as pool:
        pool.map(add_all, data)
