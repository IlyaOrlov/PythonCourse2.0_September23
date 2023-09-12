def first_relapse(lst):
    for i, relapse in enumerate(lst):
        if relapse in lst[:i]:
            return relapse
    return "повторов нет"


if __name__ == "__main__":
    lst = [2, 3, 4, 5, 3, 2]
    print(first_relapse(lst))
