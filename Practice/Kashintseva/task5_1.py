def sor(arr):
    for i in range(len(arr)):
        x = i
        for n in range(i+1, len(arr)):
            if arr[n] < arr[x]:
                x = n
                arr[i], arr[x] = arr[x], arr[i]
    return arr


arr = [2, 4, 1, 3, 16, 2, 1, 3, 9, 7]
s = sor(arr)
print(s)
