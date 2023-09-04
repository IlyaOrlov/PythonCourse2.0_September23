if __name__ == "__main__":
    stop_word = "хватит"
    respond0 = 'Введите Ваше утверждение, а если нечего сказать, введите "хватит" :  '
    respond1 = 'Ты сам-то понял, что написал? нечего сказать? введи "хватит" :  '
    respond2 = 'Аргументируй ! если нечем, то "хватит" :  '
    respond3 = 'И? хотя лучше просто введи "хватит" :  '
    question = input(respond0)
    while question != stop_word:
        question = input(respond1)
        if question == stop_word:
            break
        question = input(respond2)
        if question == stop_word:
            break
        question = input(respond3)
        if question == stop_word:
            break
    print(f"\nВы ввели слово {stop_word} ! значит я Вас переспорил")
