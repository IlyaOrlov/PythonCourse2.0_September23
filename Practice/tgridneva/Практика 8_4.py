def merge_arrays(arr1, arr2, arr3):
    return arr1 + arr2 + arr3


input_arrays = ([1, 2, 3], [4, 5], [6, 7])
result = merge_arrays(*input_arrays)
print(result)
