def delete_post(num, lst):
    for str in lst:
        if num in str:
            index = str.index(num)
            for dels in lst:
                del dels[index]
    return lst


if __name__ == "__main__":
    lst = [
        [1, 2, 3, 4, 5, 6],
        [7, 8, 9, 3, 5, 1],
        [0, 3, 7, 9, 4, 5]
        ]
    num = 7
    print(delete_post(num, lst))
