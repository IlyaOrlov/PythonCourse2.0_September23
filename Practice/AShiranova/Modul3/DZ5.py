word = input("Введите слово  : ").lower()
revers_word = word[::-1]
palindrom = word == revers_word
print(f"Ваше слово палиндром?  {palindrom}  !!!")
