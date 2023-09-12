import random


def verification_player():
    while True:
        plauer_str = input("Сделай свой ход (камень '0' бумага '1' ножницы '2') -> ")
        if (super := plauer_str.lower()) == "stop":
            return super
        elif super in ("0", "1", "2"):
            return int(super)


if __name__ == "__main__":
    array_game = ["камень", "бумага", "ножницы"]
    raund = 1
    score_ii = 0
    score_player = 0
    print("Поиграем? Серия из 10-ти раундов!\nВведи 'stop', игра закончится, ты проиграешь!")
    while raund <= 10:
        ii_input = random.randint(0, 2)
        print(f"Раунд {raund}", end="  ")
        player_input = verification_player()
        if player_input == 'stop':
            print("Вы ввели 'stop' и проиглали !")
            break
        res_raund = str(ii_input) + str(player_input)
        if ii_input != player_input:
            if res_raund in ("02", "10", "21"):
                score_ii += 1
            else:
                score_player += 1
        print(f"                   СуперМозг          Вы")
        print(f"Счёт                   {score_ii}       :       {score_player}")
        print(f"                    {array_game[ii_input]}          {array_game[player_input]}")
        raund += 1
    else:
        print("Игра окончена !")
