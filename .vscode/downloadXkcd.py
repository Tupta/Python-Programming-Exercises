#! python3
# downloadXkcd.py — Pobiera wszystkie komiksy opublikowane w witrynie XKCD.

import requests, os, bs4

url = 'http://xkcd.com'

os.makedirs('xkcd1, exist_ok=True')

while not url.endswith('#'):
    print("pobieranie strony %s..." % url)
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text)

comicElem = soup.select('#comic img')

if comicElem == []:
    print("nieudalo sie pobrac pliku obrazu z komiksu")
else:
    comicUrl = 'http:' + comicElem[0].get('src')
    print('pobieranie obrazu %s...' % (comicUrl))
    res = requests.get(comicUrl)
    res.raise_for_status()

imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')

for chunk in res.iter_content(100000):
    imageFile.write(chunk)
imageFile.close()

prevLink = soup.selected('a[rel="prev"]')[0]
url = 'http://xkcd.com' + prevLink.get('href')

print("gotowe")