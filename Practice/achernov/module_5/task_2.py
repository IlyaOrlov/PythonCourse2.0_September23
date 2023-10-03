def find_num(a):
    unique = set()
    for i in a:
        if i in unique:
            return i
        unique.add(i)


if __name__ == "__main__":
    arr = [2, 3, 4, 5, 3, 2]
    result = find_num(arr)
    print(f"Первый повторяющийся элемент: {result}")
