if __name__ == "__main__":
    lst = [0, 3, 24, 2, 3, 7]
    i = 0
    while i < len(lst):
        lst_i = lst[i:]
        first_lst = lst_i[0]
        index_min = lst_i.index(min(lst_i)) + i
        lst[i] = min(lst_i)
        lst[index_min] = first_lst
        i += 1
    print(lst)
