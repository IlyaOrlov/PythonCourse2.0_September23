import threading


def f(d):
    print(f"Данные потока {threading.current_thread().name} : {d}")


if __name__ == "__main__":
    res = [threading.Thread(target=f, args=(i + 1,)) for i in range(5)]
    for th in res:
        th.start()
    for th in res:
        th.join()
