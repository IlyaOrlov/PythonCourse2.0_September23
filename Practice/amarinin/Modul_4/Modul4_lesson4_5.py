import random


def verification_int():
    while not (str_as_num := input(" значение границы интервала ->>  ")).isdecimal():
        print(f"введено не понятно что  {str_as_num}   ", end="")
    return int(str_as_num)


def random_num(num1, num2):
    return random.randint(num1, num2) if num1 < num2 else random.randint(num2, num1)


def verification_exit_int():
    if not (exit_str := input(f"Попробуйте угадать число в "
                              f"интервале {first_interval}  :  {last_interval} включительно ->>  ")).isdecimal():
        print("\033[7mВведено любимое слово, игра окончена!\033[0m")
        return wunder_number
    return int(exit_str)


if __name__ == "__main__":
    print("Поиграем?! Если надоест, введи\033[31m любимое\033[0m слово.\nвведи границы числового интервала :")
    print("    первое", end="")
    first_interval = verification_int()
    print("    второе", end="")
    last_interval = verification_int()
    wunder_number = random_num(first_interval, last_interval)
    number = verification_exit_int()
    while number != wunder_number:
        if number > wunder_number:
            print(f"Не угадали! Ваше число {number} больше загаданного")
        else:
            print(f"Не угадали! Ваше число {number} меньше загаданного")
        number = verification_exit_int()
    else:
        print(f"Загаданное число равно {wunder_number} !!!")
