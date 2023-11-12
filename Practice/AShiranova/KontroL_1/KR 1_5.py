def func_name(test_st):
    my_count = 0
    for i in test_st:
        if i.lower() == symbol.lower():
            my_count = my_count + 1
    print("Ответ : "
          + str(my_count))


if __name__ == "__main__":
    value = input("Введите строку:")
    symbol = input("букву:")
    func_name(value)
