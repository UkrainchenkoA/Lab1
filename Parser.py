import requests
from bs4 import BeautifulSoup

def FileWrite(str, file):
    file.write(str)


def Parse():
    baseUrl = "https://www.omgtu.ru/l/?PAGEN_1={}"
    file = open("output.txt", "w", encoding='utf-8')
    for pageNumber in range(1, 158):
            url = baseUrl.format(pageNumber)
            page = requests.get(url)
            soup = BeautifulSoup(page.text, "html.parser")
            block = soup.findAll('h3', class_='news-card__title')
            for data in block:
                description = data.text
                FileWrite(description.strip() + "\n", file)
    file.close()