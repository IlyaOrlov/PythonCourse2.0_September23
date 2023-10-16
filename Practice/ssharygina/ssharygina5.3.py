game = {"Танки": "World of Tanks", "КС": "Counter-Strike", "МК": "Minecraft"}
txt = "Самые популярные игры: Танки, КС, МК"
for k, v in game.items():
    txt = txt.replace(k, v)
print(txt)
