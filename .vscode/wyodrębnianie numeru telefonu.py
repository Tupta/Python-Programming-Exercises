#Projekt — wyodrębnianie numeru telefonu i adresu e-mail
# Pobranie tekstu ze schowka.
# Wyszukanie w tekście numerów telefonów i adresów email.
# Umieszczenie znalezionych danych w schowku.
# Użycie modułu pyperclip do skopiowania i wklejenia ciągów tekstowych.
# Utworzenie dwóch wyrażeń regularnych przeznaczonych do dopasowania numeru telefonu i adresu e-mail.
# Dla obu wyrażeń regularnych wyszukanie wszystkich dopasowań, a nie tylko pierwszego.
# Eleganckie sformatowanie dopasowanych ciągów tekstowych na postać pojedynczego ciągu tekstowego przeznaczonego do umieszczenia w schowku.
# Wyświetlenie pewnego rodzaju komunikatu, jeśli w tekście nie zostaną znalezione dopasowania.


#! python3

import pyperclip, re
phoneRegex = re.compile(r'''(
(\d{3}|\(\d{3}\))? # Numer kierunkowy.
(\s|-|\.)? # Separator.
(\d{3}) # Pierwsze trzy cyfry.
(\s|-|\.) # Separator.
(\d{4}) # Ostatnie cztery cyfry.
(\s*(ext|x|ext.)\s*(\d{2,5}))? # Numer wewnętrzny.
)''', re.VERBOSE)
emailRegex = re.compile(r'''(
[a-zA-Z0-9._%+-]+ # Nazwa użytkownika szuka jednego znaku lub więcej dowolnych znaków, takich jak mała i duża litera, cyfra, kropka, znak podkreślenia, znak procentu, znak plus lub myślnik..
@ # Znak @. .
[a-zA-Z0-9.-]+ # Nazwa domeny.
(\.[a-zA-Z]{2,4}) # Kropka i później cokolwiek.
)''', re.VERBOSE)

phoneRegex = re.compile(r'''(
    text = str(pyperclip.paste())
matches = []
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)
for groups in emailRegex.findall(text):
    matches.append(groups[0])

for groups in emailRegex.findall(text):
    matches.append(groups[0])
# Skopiowanie wyników do schowka.
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Skopiowano do schowka:')
    print('\n'.join(matches))
else:
    print('Nie znaleziono żadnego numeru telefonu lub adresu email.')