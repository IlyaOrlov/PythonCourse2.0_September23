lst = [4, 5, 3, 2, 1]  # N, M << N
lst1 = [0 for _ in range(5)]  # O(M)
for x in lst:  # O(N)
    lst1[x] += 1

res = []
for i, y in enumerate(lst1):  # O(M)
    for j in range(y):  # O(M)
        res.append(i)

print(res)
# O(N) + O(M) + O(M^2) => O(N)