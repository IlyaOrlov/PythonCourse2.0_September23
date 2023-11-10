from urllib import request
import re


url = 'http://google.com'
response = request.urlopen(url)
web_page = response.read().decode()

s = re.compile(r'href="(.*?)"')
res = re.findall(s, web_page)
lst = []
for j in res:
    if j.startswith('http'):
        lst.append(j)
    else:
        lst.append(url + j)
for i in lst:
    try:
        if request.urlopen(i).getcode() == 200:
            print(f"Ссылка {i} исправна.")
    except Exception as e:
        print(f"Ссылка {i} не доступна из за {e}")
