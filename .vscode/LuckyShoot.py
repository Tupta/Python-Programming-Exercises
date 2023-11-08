#! python

# program Otwiera kilka wyników wyszukiwania Google.

# Pobranie słów kluczowych wyszukiwania z argumentów wiersza poleceń.
# Retrieve search keywords from arguments command line.

# Pobranie strony wyników wyszukiwania.
# Download the search results page.

# Otworzenie nowej karty dla każdego znalezionego wyniku.
# Open a new tab for anyone found result.

# import requests, sys, webbrowser, bs4

# # Sprawdzenie, czy są dostępne argumenty wiersza poleceń
# if len(sys.argv) < 2:
#     print("Podaj słowa kluczowe do wyszukania.")
#     sys.exit()

# print('Wyszukiwanie...')

# res = requests.get('http://google.pl/search?q=' + ''.join(sys.argv[1:]))
# res.raise_for_status()

# soup = bs4.BeautifulSoup(res.text, 'html.parser')

# linkElems = soup.select('.r a')

# numOpen = min(5, len(linkElems))

# for i in range(numOpen):
#     webbrowser.open('http://google.pl' + linkElems[i].get('href'))
    
#############################
#Wersja alternatywna

# Importowanie niezbędnych modułów
import requests
import sys
import webbrowser
import bs4

# Sprawdzenie, czy są dostępne argumenty wiersza poleceń
if len(sys.argv) < 2:
    print("Podaj słowa kluczowe do wyszukania.")
    sys.exit()

print('Wyszukiwanie...')

# Obsługa błędów podczas łączenia z Google
try:
    res = requests.get('http://google.pl/search?q=' + ''.join(sys.argv[1:]))
    res.raise_for_status()
except requests.exceptions.RequestException as e:
    print("Wystąpił błąd podczas łączenia z Google:", e)
    sys.exit()

# Analiza wyników strony Google z użyciem parsera HTML
soup = bs4.BeautifulSoup(res.text, 'html.parser')

# Wybieranie linków z wyników wyszukiwania
linkElems = soup.select('.r a')

numOpen = min(5, len(linkElems))

# Otwieranie pierwszych pięciu wyników w przeglądarce
for i in range(numOpen):
    webbrowser.open('http://google.pl' + linkElems[i].get('href'))
