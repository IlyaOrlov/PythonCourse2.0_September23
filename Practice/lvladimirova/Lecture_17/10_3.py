import threading


def thread_function(private_data):
    thread_name = threading.current_thread().name
    print("Поток:", thread_name, "Приватные данные:", private_data)


threads = []
for i in range(3):
    private_data = "Приватные данные потока " + str(i)
    thread = threading.Thread(target=thread_function, args=(private_data,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()
