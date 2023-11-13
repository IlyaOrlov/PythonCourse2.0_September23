def func_name(test_st, symbol):
    my_count = 0
    symbol_lower = symbol.lower()
    for i in test_st:
        if i.lower() == symbol_lower:
            my_count = my_count + 1
    return my_count


if __name__ == "__main__":
    value = input("Введите строку:")
    input_symbol = input("букву:")
    result = func_name(value, input_symbol)
    print(f"Ответ {result}")
