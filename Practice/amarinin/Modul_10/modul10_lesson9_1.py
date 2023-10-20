import re


def read_api(file):
    with open(file, "r", encoding="utf-8") as f:
        return f.read()


if __name__ == "__main__":
    line = read_api(r"..\..\README.md")
    print(list(set(re.findall(r'git\s[a-z]*\s-{1,2}\w+\s\w*\.*\w*', line))))
    # цикл попробую, сейча одни даты в голове )))
