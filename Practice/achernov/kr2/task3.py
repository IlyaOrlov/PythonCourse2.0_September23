def my_format(string, *args, **kwargs):
    if args:
        for i, arg in enumerate(args):
            string = string.replace("{" + str(i) + "}", str(arg))

    if kwargs:
        for key, value in kwargs.items():
            string = string.replace("{" + key + "}", str(value))

    return string


hero = "колдун"
lvl = 99
print(my_format("Привет, я {0} и я {1} уровня.", hero, lvl))
print(my_format("Я {hero} и я {age} уровня.", hero=hero, lvl=lvl))
