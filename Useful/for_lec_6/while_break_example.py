s = "aqnrnnmtm"
# i = 0
# not_found = True
# while i < len(s) and not_found:
#     if s[i].isdecimal():
#         print(f"Нашли: {i}")
#         not_found = False
#     i += 1

i = 0
while i < len(s):
    if s[i].isdecimal():
        print(f"Нашли: {i}")
        break
    i += 1
else:
    print("Числовой символ не найден")
