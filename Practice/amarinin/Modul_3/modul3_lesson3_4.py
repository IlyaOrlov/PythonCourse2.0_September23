if __name__ == "__main__":
    word = input("Введите слово, содержащее буквы 'A' : ")
    replaze_word = word.replace(chr(65), "*").replace(chr(1040), "*")
    print(replaze_word)
