#! python3


# quickWeather.py — Wyświetla prognozę pogody dla lokalizacji podanej w wierszu poleceń.

import json, requests, sys

# if len(sys.argv) < 2:
#     print('Użycie: quickWeather.py lokalizacja')
#     sys.exit()
# location = ' '.join(sys.argv[1:])

location = ('San Francisco, CA')



##################################################################
# d = ['quickWeather.py', 'San', 'Francisco,', 'CA']
# #d = ['1', '2', '3', '9']
# print(d)

# dd = ''.join(d)

#print(dd)

##################################################################

# TODO: Pobranie danych w formacie JSON z API witryny OpenWeatherMap.org.

url ='http://api.openweathermap.org/data/2.5/forecast/daily?q=%s&cnt=3' % (location)
response = requests.get(url)
response.raise_for_status()

# TODO: Umieszczenie danych JSON w zmiennej Pythona.

weatherData = json.loads(response.text)

# Wyświetlenie opisu prognozy pogody.

w = weatherData['list']
print('Aktualna pogoda w %s:' % (location))
print(w[0]['weather'][0]['main'], '-', w[0]['weather'][0]['description'])
print()
print('Jutro:')
print(w[1]['weather'][0]['main'], '-', w[1]['weather'][0]['description'])
print()
print('Pojutrze:')
print(w[2]['weather'][0]['main'], '-', w[2]['weather'][0]['description'])

