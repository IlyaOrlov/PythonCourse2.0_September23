def func_name():
    test_str = "Hi, Elvis, I am here!"
    my_count = 0
    for i in test_str:
        if i == 'i':
            my_count = my_count + 1
    print("Ответ : "
          + str(my_count))


if __name__ == "__main__":
    func_name()
