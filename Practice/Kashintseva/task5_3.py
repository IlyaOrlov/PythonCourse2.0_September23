name = {"Антонина": "Тоня", "Демид": "Дема", "Мирослава": "Мира", "Арсения": "Сеня"}
sh = "Девочка перечисляла своих друзей: Демид, Арсения, Антонина, Мирослава."
for k, v in name.items():
    sh = sh.replace(k, v)
print(sh)