arr = [0, 3, 24, 2, 3, 7]
for i in range(len(arr)):
    for n in range(i+1, len(arr)):
        if arr[n] < arr[i]:
            arr[i], arr[n] = arr[n], arr[i]
print(arr)
