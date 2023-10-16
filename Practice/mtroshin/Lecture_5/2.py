# def povtor(arr):
#     for i in range(len(arr)):
#         for j in range(0, i - 1):
#             if j < len(arr):
#                 if arr[i] == arr[j]:
#                     print(arr[i])
#                     return arr[i]

def povtor(arr):
    mnogestvo = set('')
    for i in range(len(arr)-1):
        if arr[i] in mnogestvo:
            print(arr[i])
        else:
            mnogestvo.add(arr[i])

arr = [2, 3, 4, 5, 3, 2]
povtor(arr)
