money_dict = {"USD": "доллар", "EUR": "евро", "RUB": "рубль", "CNH": "юань", "JPY": "йена"}
s = ("Национальные валюты разных стран:\n Америка - USD\n Германия - EUR\n Россия - RUB\n Китай - CNH\n Япония - JPY")
for k, v in money_dict.items():
    s = s.replace(k, v)
print(s)
