def replace_templates(string, dictionary):
    for key, value in dictionary.items():
        string = string.replace(key, value)
    return string


template_string = "Привет, {name}! Как дела, {name}? Хорошего дня, {name}!"
template_dict = {"{name}": "Илья"}

result = replace_templates(template_string, template_dict)
print(result)
