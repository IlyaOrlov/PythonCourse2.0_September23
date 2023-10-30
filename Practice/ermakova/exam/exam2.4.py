# Написать функцию copyfile: функция принимает два аргумента – имена файлов source и
# destination, открывает source, читает его, открывает destination, пишет в него. Если source не
# найден или destination уже существует, то выбрасываются соответствующие исключения. Нужно
# проверить выполнение функции как для правильных аргументов, так и для приводящих к
# исключениям.(3 балла)

def copyfile(source, destination):
    try:
        with open(source, 'r') as file:
            content = file.read()
        with open(destination, 'x') as file1:
            file1.write(content)
            print(f"Файл {source} скопирован в {destination}")
    except FileNotFoundError:
        print(f"Файл {source} не найден")
    except FileExistsError:
        print(f"Файл {destination} уже существует")


# здесь должно все записаться, если первый раз, второй раз будет
# FileExistsError
with open("source_directory/source1.txt", "w", encoding="utf-8") as f:
    f.write("Контент")
source_file = 'source_directory/source1.txt'
destination_file = 'destination_directory/destination1.txt'
copyfile(source_file, destination_file)

# здесь FileNotFoundError
source_file1 = 'source2.txt'
destination_file1 = 'destination2.txt'
copyfile(source_file1, destination_file1)
