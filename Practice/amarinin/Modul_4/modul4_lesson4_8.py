import random


def verification_player():
    while True:
        plauer_str = input("Сделай свой ход (камень '0' бумага '1' ножницы '2') -> ")
        match plauer_str.lower():
            case "0":
                return 0
            case "1":
                return 1
            case "2":
                return 2
            case "stop":
                return "stop"


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
        match res_raund:
            case "02":
                score_ii += 1
            case "10":
                score_ii += 1
            case "21":
                score_ii += 1
            case "01":
                score_player += 1
            case "12":
                score_player += 1
            case "20":
                score_player += 1
        print(f"                   СуперМозг          Вы")
        print(f"Счёт                   {score_ii}       :       {score_player}")
        print(f"                    {array_game[ii_input]}          {array_game[player_input]}")
        raund += 1
    else:
        print("Игра окончена !")
