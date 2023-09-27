if __name__ == "__main__":
    my_dict = {"пиво": "beer", "вода": "water", "не": "not"}
    s = "Губит людей не пиво, губит людей вода."
    print(s)
    for str_keys, str_replace in my_dict.items():
        s = s.replace(str_keys, str_replace)
    print(s)
