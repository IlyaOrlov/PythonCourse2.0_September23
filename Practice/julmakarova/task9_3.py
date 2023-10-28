import os
import shutil
import time


def watch_delete(path):
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
        print("Путь к папке указан некорректно!")


my_path = r'C:\Users\Юлия\PycharmProjects\PythonCourse2.0_September23\Practice\julmakarova\test_9_3'

your_path = input("Укажите путь до папки, за которой предполагается наблюдение: ")
watch_delete(your_path)
