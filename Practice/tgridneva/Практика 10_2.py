import threading


def add_arguments(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return a + b
    elif isinstance(a, str) and isinstance(b, str):
        return a + b
    elif isinstance(a, list) and isinstance(b, list):
        return a + b
    else:
        raise ValueError("Unsupported argument types")


argument_sets = [
    (1, 2),
    ("Hello, ", "world!"),
    ([1, 2, 3], [4, 5, 6])
]

threads = []
results = []

for args in argument_sets:
    thread = threading.Thread(target=lambda: results.append(add_arguments(*args)))
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

for result in results:
    print("Result:", result)
