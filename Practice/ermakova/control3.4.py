word = input("Введите слово: ")
# русский и английский алфавит
if "А" in word or "а" in word or "A" in word or "a" in word:
    word1 = (word.replace("а", "*").replace("А", "*")
             .replace("a", "*").replace("A", "*"))
    print(f"Итоговый результат: {word1}")
else:
    print(f"В данном слове нет буквы А!")
