import requests
from bs4 import BeautifulSoup
import re
import time
import datetime


def scraper():
    # lädt bekannte artikel
    knownAs = []
    with open('knowArticles', 'r') as fh:
        for line in fh:
            knownAs.append(line.split(';')[0])

    # lädt artikel auf der orf seite
    response = requests.get('https://orf.at/')

    soup = BeautifulSoup(response.content, "html.parser")

    links = soup.find_all('a')

    raw_urls = []
    urls = []
    known_urls = []
    for link in links:
        raw_urls.append(link.get('href'))

    for url in raw_urls:
        if 'stories' in url and url not in known_urls:
            if re.search(r'[A-Za-z:\/\.]*.stories\/\d+\/', url):
                urls.append(url)

    new_url = []
    # gleicht artikel mit bekannten ab
    for url in urls:
        if url not in knownAs[knownAs.__len__() - 100:]:
            knownAs.append(url)
            new_url.append(url + ';' + str(time.time()) + '\n')

    # download artikel

    for url in new_url:
        url = url.split(';')[0]
        # print(url)
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        dir = 'Artikel\\' + str(re.findall(r'\d+', url)[0]) + '.html'
        with open(dir, 'w', encoding='UTF-8') as fh:
            fh.write(soup.prettify())

    # update known articles mit zeiten
    with open('knowArticles', 'a') as fh:
        for url in new_url:
            fh.write(url)

scraper()
'''while True:
    scraper()
    time.sleep(300)
'''