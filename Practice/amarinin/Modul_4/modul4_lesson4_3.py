if __name__ == "__main__":
    number = ""
    full_number = ""
    incorrect_input = ""
    while number != 'stop':
        full_number = full_number + number
        print(f" Ваше число : {full_number}     ", incorrect_input, end="")
        number = input("-> Введите цифру (цифры) или слово 'stop' : ").lower()
        if number.isdigit() == False and number != 'stop':
            incorrect_input = "НЕ КОРРЕКТНЫЙ ВВОД  <" + number + ">   "
            number = ""
        else:
            incorrect_input = ""
