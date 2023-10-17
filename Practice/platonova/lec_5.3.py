def replace_text(text, dictionary):
    for key, value in dictionary.items():
        text= text.replace(key, str(value))
    return text


text = "Добрый день, {name}! Ваш табельный номер {count} ."
dictionary = {"{name}": "Юля", "{count}": 2}

result = replace_text(text, dictionary)
print(result)
