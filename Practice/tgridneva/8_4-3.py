import itertools


def generate_password_combinations():
    password = 'password'
    combinations = list(itertools.permutations(password))
    return combinations


result = generate_password_combinations()
for combination in result:
    print(combination)
