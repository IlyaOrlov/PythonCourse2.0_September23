def change_templates(string, replace_dict):
    for template, replacement in replace_dict.items():
        string = string.replace(template, replacement)
    return string


if __name__ == "__main__":
    my_text = "Привет, {name}! Так когда-то сказала мне {singer}."
    replacement_dict = {"{name}": "Андрей", "{singer}": "Ирина Аллегрова"}
    result_string = change_templates(my_text, replacement_dict)
    print(result_string)
