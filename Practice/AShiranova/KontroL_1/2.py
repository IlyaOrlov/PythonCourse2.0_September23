def my_reverse(my_list):
    last_index = len(my_list) - 1
    half_size = len(my_list) // 2
    for i in range(0, half_size):
        my_list[last_index], my_list[i] = my_list[i], my_list[last_index]
        last_index -= 1
    return my_list


if __name__ == "__main__":
    value = [1, 2, 3, 4, 5, 6, 7]
    print(my_reverse(value))
