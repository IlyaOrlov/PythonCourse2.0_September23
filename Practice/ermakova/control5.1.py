arr = [0, 3, 24, 2, 3, 7]
for i in range(len(arr)-1):
    x_min = i
    for n in range(i+1, len(arr)):
        if arr[n] < arr[x_min]:
            x_min = n
    if i != x_min:
        arr[i], arr[x_min] = arr[x_min], arr[i]
print(arr)
