from random import randint


def list_random(post_list=5):
    return [randint(0, 9) for _ in range(post_list)]


def first_relapse(test_list):
    for i, relapse in enumerate(test_list):
        if test_list.index(relapse, 0) < i:
            return relapse
    return None


if __name__ == "__main__":
    test_lst = list_random(10)
    print(test_lst)
    print(first_relapse(test_lst))
