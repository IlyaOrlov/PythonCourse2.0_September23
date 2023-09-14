arr = [2, 4, 1, 16, 9, 7]
for i, n in enumerate(arr):
    x = arr.index(min(arr[i::]))
    arr[i], arr[x] = arr[x], arr[i]
    print(arr)
