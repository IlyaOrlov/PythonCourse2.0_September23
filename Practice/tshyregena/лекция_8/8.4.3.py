import itertools

letters = "password"
perms = itertools.permutations(letters)

for perm in perms:
    print(perm)
