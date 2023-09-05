import random

def verification_str_int (input_str):
    if input_str.isdecimal() is False:
        print("\033[7mвведено не понятно что, игра окончена!\033[0m")
        exit()
    return int(input_str)


if __name__ == "__main__":
    stop_word = ""
    print("Поиграем?! Если надоест, введи\033[31m любимое\033[0m слово\nВведи границы числового интервала :")
    min_interval = input("    минимальное значение границы интервала (\033[31mцелое положительное число\033[0m) ->>  ")
    min_interval = verification_str_int(min_interval)
    max_interval = input("    максимальное значение границы интервала (\033[31mцелое положительное число\033[0m) ->>  ")
    max_interval = verification_str_int(max_interval)
    wunder_number = random.randint(min_interval, max_interval)
    number = input(f"Попробуйте угадать число в интервале от {min_interval} до {max_interval} включительно ->>  ")
    number = verification_str_int(number)
    while  number != wunder_number:
        if number > wunder_number:
            number = input(f"Не угадали! Продолжим, Ваше число {number} больше загаданного, попробуйте еще раз ->>  ")
            number = verification_str_int(number)
        if number < wunder_number:
            number = input(f"Не угадали! Продолжим, Ваше число {number} меньше загаданного, попробуйте еще раз ->>  ")
            number = verification_str_int(number)
    print(f"Игра окончена, Вы угадали число {wunder_number} !!!")

