import re


def g_com(file):
    with open(file, "r", encoding="utf-8") as f:
        return f.read()


if __name__ == "__main__":
    line = g_com(r"C:\Users\user\PycharmProjects\PythonCourse2.0_September23\Practice\README.md")
    print(list(set(re.findall(r'git\s[a-z]*\s-{1,2}\w+\s\w*\.*\w*', line))))
