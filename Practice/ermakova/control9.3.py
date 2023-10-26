import os
import shutil
import time


def delete_fun(way):
    for super_dirs, dirs, files in os.walk(way):
        for f in files:
            f_path = os.path.join(super_dirs, f)
            f_age = time.time()-os.path.getctime(f_path)
            if f_age > 60:
                os.remove(f_path)
        for d in dirs:
            d_path = os.path.join(super_dirs, d)
            d_age = time.time()-os.path.getctime(d_path)
            if d_age > 120:
                shutil.rmtree(d_path)


w = r'C:\Users\User\PycharmProjects\PythonCourse2.0_September23\Practice\ermakova\prob'
try:
    while True:
        delete_fun(w)
except KeyboardInterrupt:
    print(f"Программа остановлена")
