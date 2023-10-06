lst = [4, 5, 34, 78]  # N
for k in range(len(lst)):  # O(N)
    nM = k
    for i in range(k + 1, len(lst)):  # O(N)
        if lst[i] < lst[nM]:
            nM = i
    lst[k], lst[nM] = lst[nM], lst[k]
print(lst)

# O(N) * O(N) => O(N^2)
lst.sort()  # O(n*logN) | O(N^2)