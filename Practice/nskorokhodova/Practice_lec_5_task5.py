def change(file_path, x):
    with open(file_path, 'r') as f:
        content = f.read()
    if x == "развернуть":
        content = content.replace('\t', '    ')
    elif x == "свернуть":
        content = content.replace('    ', '\t')
    else:
        print("Некорректный ввод")

    with open(file_path, 'w') as f:
        f.write(content)


my_file = input("Введите путь к файлу: ")
x = input("Выберите развернуть или свернуть: ")
change(my_file, x)
