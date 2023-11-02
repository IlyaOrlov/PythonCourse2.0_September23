import threading


def hold(data):
    print(f'Имя потока: {threading.current_thread().name}, хранит данные: {data}')


d = ("Иван Иванов", "30 лет", "Высшее образование")
threads = []
for i in range(3):
    thr = threading.Thread(target=hold, args=(d,))
    thr.start()
    threads.append(thr)

for thr in threads:
    thr.join()
