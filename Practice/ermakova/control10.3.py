import threading


def name_private(pr):
    thread_name = threading.current_thread().name
    print(f"Thread name: {thread_name}, nickname: {pr}")


if __name__ == "__main__":
    for args in (("Морж",), ("Компот",), ("Кислый",)):
        t = []
        thr = threading.Thread(target=name_private, args=args)
        thr.start()
        t.append(thr)
    for n in t:
        n.join()
