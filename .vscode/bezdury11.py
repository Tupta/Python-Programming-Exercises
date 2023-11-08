for i in range(4
):
    print(i+1)

#! python3
# randomQuizGenerator.py — Tworzy quiz wraz z pytaniami i odpowiedziami
# ułożonymi w losowej kolejności wraz z odpowiedziami.

import random

# To są dane quizu. Klucze to nazwy stanów, natomiast wartości to ich stolice. Wszystko zamkniete w zmiennej capitals
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau',
'Arizona': 'Phoenix',
'Arkansas': 'Little Rock', 'Kalifornia': 'Sacramento',
'Kolorado': 'Denver',
'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Floryda':
'Tallahassee',
'Georgia': 'Atlanta', 'Hawaje': 'Honolulu', 'Idaho': 'Boise',
'Illinois':
'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines',
'Kansas':
'Topeka', 'Kentucky': 'Frankfort', 'Luizjana': 'Baton Rouge',
'Maine':
'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston',
'Michigan':
'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson',
'Missouri':
'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln',
'Nevada':
'Carson City', 'New Hampshire': 'Concord', 'New Jersey':
'Trenton', 'Nowy Meksyk': 'Santa Fe', 'Nowy Jork': 'Albany', 'Karolina Północna':
'Raleigh',
'Dakota Północna': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma':
'Oklahoma City',
'Oregon': 'Salem', 'Pensylwania': 'Harrisburg', 'Rhode Island':
'Providence',
'Karolina Południowa': 'Columbia', 'Dakota Południowa': 'Pierre',
'Tennessee':
'Nashville', 'Teksas': 'Austin', 'Utah': 'Salt Lake City',
'Vermont':
'Montpelier', 'Wirginia': 'Richmond', 'Waszyngton': 'Olympia',
'Wirginia Zachodnia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming':
'Cheyenne'}

states = list(capitals.keys())

print(states)
random.shuffle(states)
print (states)

gd = [1,2,3,4,5,6,7,8,9]
random.shuffle(gd)
print(gd)

random.