# In: lst = [2, 3, 1, 4, 5]   N == len(lst)
# Out: 1
lst = [2, 3, 1, 4, 5]
# print(min(lst))
# 0) local_min = lst[0], local_min_idx = 0
# 1) local_min = 2 < 1 lst[1], local_min_idx = 0
# 2) local_min = 1 > 2 lst[2], local_min_idx = 2
# 3) local_min = 1 < 4 lst[3], local_min_idx = 2
# 4) local_min = 1 < 5 lst[4], local_min_idx = 2
# local_min = 1, local_min_idx = 2
# local_min ? lst[i], где 0 <= i <= 4
local_min = None
i = 0
while i < len(lst):
    if local_min is None:
        local_min = lst[i]
    else:
        if lst[i] < local_min:
            local_min = lst[i]
    i += 1
# Время: O(N)
# Память: O(1)
local_min = None
for x in lst:
    if local_min is None:
        local_min = x
    else:
        if x < local_min:
            local_min = x

print(local_min)
