def reverse_list(my_list):
    new_list = []
    for element in my_list:
        new_list.insert(0, element)
    return new_list


n = [1, 2, 3, 4, 5, 6, 7]
print(reverse_list(n))
