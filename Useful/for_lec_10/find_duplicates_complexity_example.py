def fun_find_dup(lst):  # O(N) * O(N/2) => O(N^2)
    for i in range(len(lst) - 1):  # O(N)
        for j in range(i + 1, len(lst)):  # O(N/2)
            if lst[j] == lst[i]:
                return lst[j]

def fun_find_dup1(lst):  # O(N) * O(1) => O(N)
    s = set()
    for i in range(len(lst)):  # O(N)
        if lst[i] in s:  # O(1)
            return lst[i]
        else:
            s.add(lst[i])


print(fun_find_dup1([1, 2, 4, 3, 2, 1]))
print(fun_find_dup1([1, 2, 3]))

# for i in range(len(lst) - 1):
#     for j in range(i + 1, len(lst)):
#         if lst[j] == lst[i]:
#             print(lst[j])
#             break
#     else:
#         continue
#     break