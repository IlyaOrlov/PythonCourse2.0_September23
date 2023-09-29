slovo1 = input("Введите слово, содержащее буквы А: ")
slovo2 = slovo1.replace(chr(65), "*").replace(chr(1040), "*")
print(f"Результат: {slovo2}")
