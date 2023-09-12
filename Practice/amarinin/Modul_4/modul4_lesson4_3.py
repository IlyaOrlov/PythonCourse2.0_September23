if __name__ == "__main__":
    number = ""
    full_number = ""
    incorrect_input = ""
    stop = number != 'stop'
    while stop:
        full_number = full_number + number
        print(f"Ваше число : {full_number}       {incorrect_input}", end="")
        number = input("-> Введите цифру (цифры) или слово 'stop' : ").lower()
        if number == 'stop':
            break
        elif not number.isdecimal():
            incorrect_input = f"НЕ КОРРЕКТНЫЙ ВВОД  <{number}>   "
            number = ""
        else:
            incorrect_input = ""
    print(f"\nВы ввели слово {number}, Ваше число :   {full_number}")
