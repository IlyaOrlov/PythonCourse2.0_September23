# Два потока запрашивают и выводят координаты точки на плоскости
from threading import Thread, RLock
import time

# GIL


class Base:
    x = 0
    y = 0


def print_fun():
    i = 0
    while i < 2:
        lock.acquire()
        Base.x = input("2x: ")
        Base.y = input("2y: ")
        print(f'Thread 2: Base.x = {Base.x}, Base.y = {Base.y}')
        i += 1
        time.sleep(1)
        lock.release()


if __name__ == '__main__':
    lock = RLock()
    t = Thread(target=print_fun)
    t.start()
    i = 0
    while i < 2:
        lock.acquire()  # CAS: compare and swap
        Base.x = input("1x: ")
        Base.y = input("1y: ")
        print(f'Thread 1: Base.x = {Base.x}, Base.y = {Base.y}')
        i += 1
        time.sleep(1)
        lock.release()

    t.join()
