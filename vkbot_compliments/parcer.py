from bs4 import BeautifulSoup
import requests


def parce():
    URL = 'https://heaclub.ru/100-luchshih-samyh-krasivyh-komplimentov-devushke-i-zhenshhine-o-ee-krasote-svoimi-slovami-v-proze-spisok-kak-krasivo-skazat-devushke-chto-ona-krasivaya-stishki-chetverostishya-pro-krasotu-devus'
    HEADERS = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 YaBrowser/21.9.0.1044 Yowser/2.5 Safari/537.36'
    }

    response = requests.get(URL, headers=HEADERS)
    soup = BeautifulSoup(response.content, 'html.parser')
    t1 = soup.find('div', class_="entry-content")
    it1 = t1.find('ol', class_="")
    it2 = it1.findAll('li')
    compls = []
    for comp in it2:
        compls.append(comp.text)
    return compls


parce()
