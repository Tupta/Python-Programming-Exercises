#! python3
# searchpypi.py — Otwiera kilka wyników wyszukiwania w Python Package Index.

import requests, sys, webbrowser, bs4

print('Wyszukiwanie...')  # Komunikat wyświetlany podczas pobierania strony wyników wyszukiwania.
res = requests.get('http://pypi.org/search/?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()

# Pobranie łączy z kilkoma pierwszymi wynikami wyszukiwania.
soup = bs4.BeautifulSoup(res.text, features='html.parser')
# Otworzenie karty przeglądarki WWW dla każdego wyniku wyszukiwania.
linkElems = soup.select('.package-snippet')
numOpen = min(5, len(linkElems))
for i in range(numOpen):
    urlToOpen = 'http://pypi.org' + linkElems[i].get('href')
    print('Otwieranie', urlToOpen)
    webbrowser.open(urlToOpen)
