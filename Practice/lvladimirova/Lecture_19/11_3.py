import urllib.request
import urllib.parse
from urllib.error import URLError
import re


def collect_links(url):
    response = urllib.request.urlopen(url)
    links = re.findall(r'href="([^"]*h[^"]*)">', response.read().decode('utf-8'))
    return links


def check_links(links):
    for link in links:
        try:
            url = urllib.parse.urljoin('http://google.com/', link)
            response = urllib.request.urlopen(url)
            if response.getcode() == 200:
                print(f"Ссылка {link} рабочая")
            else:
                print(f"Ссылка {link} возвращает ошибку {response.getcode()}")
        except URLError:
            print(f"Не удалось подключиться к ссылке {link}")


base_url = "http://google.com"
links = collect_links(base_url)
check_links(links)
