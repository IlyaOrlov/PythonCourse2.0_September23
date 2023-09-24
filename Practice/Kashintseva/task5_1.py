def sor(arr):
    for i in range(len(arr)):
        for n in range(i+1, len(arr)):
            if arr[n] < arr[i]:
                x = n
                arr[i], arr[x] = arr[x], arr[i]
            else:
                x = i
    return arr


arr = [2, 4, 1, 3, 16, 2, 1, 3, 9, 7]
s = sor(arr)
print(s)
