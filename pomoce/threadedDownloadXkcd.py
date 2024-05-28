#! python3
# multidownloadXkcd.py - Pobiera wszystkie komiksy opublikowane w witrynie 
# XKCD, używając do tego wielu wątków.


import requests, os, bs4, threading
os.makedirs('xkcd', exist_ok=True)  # Komiksy są przechowywane w katalogu ./xkcd.

def downloadXkcd(startComic, endComic):
    for urlNumber in range(startComic, endComic):
        # Pobranie strony.
        print('Pobieranie strony https://xkcd.com/%s...' % (urlNumber))
        res = requests.get('https://xkcd.com/%s' % (urlNumber))
        res.raise_for_status()

        soup = bs4.BeautifulSoup(res.text, 'html.parser')

        # Ustalenie adresu URL pliku obrazu komiksu.
        comicElem = soup.select('#comic img')
        if comicElem == []:
            print('Nie udało się odnaleźć pliku obrazu komiksu.')
        else:
            comicUrl = comicElem[0].get('src')
            # Pobranie obrazu.
            print('Pobranie obrazu %s...' % (comicUrl))
            res = requests.get('https:' + comicUrl)
            res.raise_for_status()

            # Zapis obrazu w katalogu ./xkcd.
            imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
            for chunk in res.iter_content(100000):
                imageFile.write(chunk)
            imageFile.close()

# Utworzenie i uruchomienie obiektów Thread.
downloadThreads = []         # Lista wszystkich obiektów Thread.
for i in range(0, 140, 10):  # Iteracja 14 razy, co powoduje utworzenie 14 wątków.
    start = i
    end = i + 9
    if start == 0:
        start = 1  # Nie istnieje komiks zerowy, stąd zdefiniowanie wartości 1.
    downloadThread = threading.Thread(target=downloadXkcd, args=(start, end))
    downloadThreads.append(downloadThread)
    downloadThread.start()

# Zaczekanie na zakończenie działania wszystkich wątków.
for downloadThread in downloadThreads:
    downloadThread.join()
print('Gotowe!')
