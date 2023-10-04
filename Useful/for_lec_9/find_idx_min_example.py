def find_min(lst):
    local_min = None
    local_min_idx = None
    for i in range(len(lst)):
        if local_min is None:
            local_min = lst[i]
            local_min_idx = i
        else:
            if lst[i] < local_min:
                local_min = lst[i]
                local_min_idx = i
    return local_min, local_min_idx

print(f"{find_min([2, 3, 1, 4, 5])}")
print(f"{find_min([2, 10, 8, 0, 1, 4, 5])}")
print(f"{find_min([])}")