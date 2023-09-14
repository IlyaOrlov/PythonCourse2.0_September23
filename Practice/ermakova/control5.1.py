arr = [0, 3, 24, 2, 3, 7]
for i in range(len(arr)-1):
    for n in range(i+1, len(arr)):
        x_min = i
        if arr[n] < arr[i]:
            x_min = n
        arr[i], arr[x_min] = arr[x_min], arr[i]
print(arr)
