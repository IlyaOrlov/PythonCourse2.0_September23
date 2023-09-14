from random import randint


def list_random(post_list=5):
    return [randint(0, 9) for _ in range(post_list)]


def first_relapse(lst):
    for i, relapse in enumerate(lst):
        if lst.index(relapse, 0) < i:
            return relapse
    return None


if __name__ == "__main__":
    lst = list_random(10)
    print(lst)
    print(first_relapse(lst))
