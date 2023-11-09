from urllib import request
import re


if __name__ == "__main__":
    req = request.Request('http://google.com')
    response = request.urlopen(req)
    web_page = response.read().decode()
    supp = (x for i in web_page.split() if len(x := re.findall(r'href="http.?://.*"', i)))
    supp_norm_list = [i[0].replace("href=", '').replace("\"", "") for i in supp]
    for i in supp_norm_list:
        try:
            a = request.Request(i)
            b = request.urlopen(a)
            print(i, "\n статус ", b.getcode())
        except Exception:
            print(i, "\n что то здесь не так")
