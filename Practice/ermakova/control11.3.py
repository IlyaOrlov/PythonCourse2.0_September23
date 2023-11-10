from urllib import request
import re


url = 'http://google.com'
response = request.urlopen(url)
web_page = response.read().decode()

s = re.compile(r'href="(.*?)"')
res = re.findall(s, web_page)
for j in res:
    try:
        if j.startswith('http'):
            if request.urlopen(j).getcode() == 200:
                print(f"Ссылка {j} исправна.")
        else:
            if request.urlopen(url + j).getcode() == 200:
                print(f"Ссылка {url + j} исправна.")
    except Exception as e:
        print(f"Ссылка {j} не доступна из-за {e}")
