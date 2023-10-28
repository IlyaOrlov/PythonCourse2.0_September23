import re


if __name__ == "__main__":
    lst = ["public", "_protected", "__private", "_attr"]
    p = re.compile("^_[^_].*")
    # p = re.compile(r'^_{1}[a-z]+')
    for i in lst:
        if res := re.findall(p, i):
           print(res)
