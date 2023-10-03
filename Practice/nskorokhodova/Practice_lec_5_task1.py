arr = [0, 3, 24, 2, 3, 7]
for i in range(len(arr)):
    min_i = i
    for x in range(i + 1, len(arr)):
        if arr[x] < arr[min_i]:
            min_i = x
    if min_i != i:
        arr[i], arr[min_i] = arr[min_i], arr[i]
print(f"Cписок отсортирован : {arr}")
