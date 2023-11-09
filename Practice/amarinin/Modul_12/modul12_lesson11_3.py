from urllib import request
import re


if __name__ == "__main__":
    req = request.Request('http://google.com')
    response = request.urlopen(req)
    web_page = response.read().decode()
    supp = (re.findall(r'href="(h.*?)"', web_page))
    for i in supp:
        try:
            a = request.Request(i)
            b = request.urlopen(a)
            print(i, "\n статус ", b.getcode())
        except Exception:
            print(i, "\n что то здесь не так")
