import concurrent.futures


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

results = []


def process_arguments(args):
    result = add_arguments(*args)
    return result


with concurrent.futures.ThreadPoolExecutor() as executor:
    futures = [executor.submit(process_arguments, args) for args in argument_sets]
    results = [future.result() for future in concurrent.futures.as_completed(futures)]

print("Results:", results)
