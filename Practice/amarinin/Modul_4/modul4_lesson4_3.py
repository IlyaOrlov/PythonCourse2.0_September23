if __name__ == "__main__":
    stop_word = 'stop'
    number = ""
    full_number = ""
    incorrect_input = ""
    while number != stop_word:
        full_number = full_number + number
        print(f"Ваше число : {full_number}       {incorrect_input}", end="")
        number = input("-> Введите цифру (цифры) или слово 'stop' : ").lower()
        if number.isdecimal() == False and number != 'stop':
            incorrect_input = f"НЕ КОРРЕКТНЫЙ ВВОД  <{number}>   "
            number = ""
        else:
            incorrect_input = ""
    print(f"\nВы ввели слово {number}, Ваше число :   {full_number}")
