word = "арзамас"
print(len(word)) # узнал сколько в слове символов

for el in range(len(word)): # перебрал слово в цикле
    print(el,[0,7])

if word[el] == "а": #проверили каждую букву на соответствие букве а
   word[el] = "*"



