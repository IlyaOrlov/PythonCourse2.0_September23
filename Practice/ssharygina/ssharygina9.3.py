import os
import shutil
import time


def del_f(path):
    if os.path.exists(path):
        while True:
            for d_path, d_names, f_names in os.walk(path):
                for f_name in f_names:
                    f_path = os.path.join(d_path, f_name)
                    if time.time() - os.path.getctime(f_path) > 60:
                        os.remove(f_path)
                for d_name in d_names:
                    d_path = os.path.join(d_path, d_name)
                    if time.time() - os.path.getctime(d_path) > 120:
                        shutil.rmtree(d_path)
    else:
        print("Путь до папки указан не верно!")


# Путь до папки для тестирования: C:\Users\user\PycharmProjects\PythonCourse2.0_September23\Practice\ssharygina\dir2
path1 = input("Укажите путь до папки, за которой необходимо следить: ")
del_f(path1)
