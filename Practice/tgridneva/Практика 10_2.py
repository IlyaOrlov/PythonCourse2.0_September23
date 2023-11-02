import time
import threading
import multiprocessing


def add_numbers(a, b):
    return a + b


def add_strings(a, b):
    return a + b


def add_lists(a, b):
    return a + b


start_time = time.time()
result1 = add_numbers(1, 2)
result2 = add_strings("Hello, ", "world!")
result3 = add_lists([1, 2, 3], [4, 5, 6])
end_time = time.time()
sequential_time = end_time - start_time

start_time = time.time()
thread1 = threading.Thread(target=add_numbers, args=(1, 2))
thread2 = threading.Thread(target=add_strings, args=("Hello, ", "world!"))
thread3 = threading.Thread(target=add_lists, args=([1, 2, 3], [4, 5, 6]))
thread1.start()
thread2.start()
thread3.start()
thread1.join()
thread2.join()
thread3.join()
end_time = time.time()
thread_time = end_time - start_time

start_time = time.time()
process1 = multiprocessing.Process(target=add_numbers, args=(1, 2))
process2 = multiprocessing.Process(target=add_strings, args=("Hello, ", "world!"))
process3 = multiprocessing.Process(target=add_lists, args=([1, 2, 3], [4, 5, 6]))
process1.start()
process2.start()
process3.start()
process1.join()
process2.join()
process3.join()
end_time = time.time()
process_time = end_time - start_time

print("Sequential Execution Time:", sequential_time)
print("Thread Execution Time:", thread_time)
print("Process Execution Time:", process_time)
