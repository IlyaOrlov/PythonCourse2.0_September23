from concurrent.futures import ThreadPoolExecutor


def add_function(args):
    a, b = args
    if isinstance(a, int) and isinstance(b, int):
        return a + b

    if isinstance(a, str) and isinstance(b, str):
        return f'{a} {b}'

    if isinstance(a, list) and isinstance(b, list):
        return a + b


my_args = [(1, 2), ("good", "day"), ([1, 2, 3], [4, 5, 6])]

with ThreadPoolExecutor() as executor:
    results = executor.map(add_function, my_args)
for result in results:
    print(result)
