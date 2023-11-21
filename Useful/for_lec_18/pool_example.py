from multiprocessing import Pool
import time
import os


lst = []

def cube(x):
    lst.append(x)
    print(f"This process {os.getpid()} processed values {lst}")
    time.sleep(2)
    res = x**3
    print(res)
    return res


# if __name__ == '__main__':
#     with Pool(processes=3) as pool:
#         for i in range(1, 7):
#             pool.apply_async(cube, (i, ))
#         pool.close()
#         pool.join()

if __name__ == '__main__':
    with Pool(processes=3) as pool:
        res = pool.map(cube, range(1,7))
        print(res)
