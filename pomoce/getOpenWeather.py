#! python3
# getOpenWeather.py - Wyświetla prognozę pogody dla lokalizacji podanej w wierszu poleceń.

import json, requests, sys

APPID = 'TWÓJ_IDENTYFIKATOR_APLIKACJI'

# Ustalenie lokalizacji na podstawie argumentów wiersza poleceń.
if len(sys.argv) < 2:
    print('Użycie: getOpenWeather.py nazwa_miasta dwuliterowy_kod_kraju')
    sys.exit()
location = ' '.join(sys.argv[1:])

# Pobranie danych w formacie JSON z API witryny OpenWeatherMap.org.
url ='http://api.openweathermap.org/data/2.5/forecast/daily?q=%s&cnt=3&APPID=%s' % (location, APPID)
response = requests.get(url)
response.raise_for_status()

# Umieszczenie danych JSON w zmiennej Pythona.
weatherData = json.loads(response.text)

# Usuń znak komentarza z następnego wiersza, 
# aby zobaczyć niezmodyfikowane dane w formacie JSON.
#print(response.text)

w = weatherData['list']
print('Aktualna pogoda w  %s:' % (location))
print(w[0]['weather'][0]['main'], '-', w[0]['weather'][0]['description'])
print()
print('Jutro:')
print(w[1]['weather'][0]['main'], '-', w[1]['weather'][0]['description'])
print()
print('Pojutrze:')
print(w[2]['weather'][0]['main'], '-', w[2]['weather'][0]['description'])
