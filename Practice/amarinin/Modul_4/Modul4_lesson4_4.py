if __name__ == "__main__":
    stop_word = "хватит"
    respond0 = 'Введите Ваше утверждение, а если нечего сказать, введите "хватит" :  '
    respond1 = 'Ты сам-то понял, что написал? нечего сказать? введи "хватит" :  '
    respond2 = 'Аргументируй ! если нечем, то "хватит" :  '
    respond3 = 'И? хотя лучше просто введи "хватит" :  '
    responds = (respond1, respond2, respond3)
    question = input(respond0)
    i = 0
    while question != stop_word:
        question = input(responds[i])
        if i >= len(responds) - 1:
            i = 0
        else:
            i += 1
    print(f"\nВы ввели слово {stop_word} ! значит я Вас переспорил")
