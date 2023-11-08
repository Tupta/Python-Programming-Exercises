#! python3

#Program zmienia nazwę pliku wraz z datą w formacie amerykańskim (MM-DD-RRRR) na datę w formacie europejskim (DD-MM-RRRR).

import shutil, os, re

# Utworzenie wyrażenia regularnego dopasowującego pliki zawierające w nazwie datę w formacie amerykańskim.

# datePattern = re.compile(r'"""^(.*?) #cały tekst przed datą
#                          ((0|2)?\d) - # jedna lub dwie cyfry okreśłające miesiąc
#                          ((0|1|2|3)?\d) - # jedna lub dwie cyfry okreśłające dzień
#                          ((19|20)\d\d) # cztery cyfry okreśłające rok
#                          (.*?)$ #cały tekst po dacie.
#                          """', re.VERBOSE)

datePattern = re.compile(r'"""^(.*?)((0|2)?\d) - ((0|1|2|3)?\d) - ((19|20)\d\d)(.*?)$"""', re.VERBOSE)
                       
# Iteracja przez pliki znajdujące się w katalogu roboczym.

for amerFilename in os.listdir('.'):
    mo = datePattern.search(amerFilename)

# Pominiecie plikow bez daty
    if mo is None:
        continue


    # Pobranie psozczegolnych fragmentów nazw pliku

    beforePart = mo.group(1)
    monthPart = mo.group(2)
    dayPart = mo.group(4)
    yearPart = mo.group(6)
    afterPart = mo.group(8)

dataPattern = re.compile(r"""^(1)(2(3) ) -(4(5) ) - (6(7)) (8)$""", re.VERBOSE)


# Przygotowanie nazwy pliku zawierającej datę w formacie europejskim.

euroFilename = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart


# Pobranie pełnych, bezwzględnych ścieżek dostępu do pliku.

absWorkingDir = os.path.abspath('.')
amerFilename = os.path.join(absWorkingDir, amerFilename)
euroFilename = os.path.join(absWorkingDir, euroFilename)

# Zmiana nazwy plików.

print('Renaming "%s" to "%s"...' % (amerFilename, euroFilename))


# Usuń znak komentarza w poniższym poleceniu, po zakończeniu testów, inaczej program tylko wyswietli liste plikow ale nie podmieni ich.
#shutil.move(amerFilename, euroFilename) 



# poniżej alternatywna krótsza wersja:

# import re
# import os
# import shutil

# # Utworzenie wyrażenia regularnego do dopasowania wzorca daty w stylu amerykańskim
# date_pattern = re.compile(r"""^(.*?) # Grupa przechwytująca dowolny tekst przed datą
#                              (\d{2}) # Grupa przechwytująca dwie cyfry oznaczające miesiąc
#                              (\d{2}) # Grupa przechwytująca dwie cyfry oznaczające dzień
#                              (\d{4}) # Grupa przechwytująca cztery cyfry oznaczające rok
#                              (.*?)$  # Grupa przechwytująca dowolny tekst po dacie
#                              """, re.VERBOSE)

# # Wywołanie funkcji os.listdir() w celu wyszukania wszystkich plików w bieżącym katalogu roboczym
# file_list = os.listdir()

# # Iteracja przez wszystkie nazwy plików
# for file_name in file_list:
#     # Użycie wyrażenia regularnego do sprawdzenia, czy nazwa pliku zawiera datę w stylu amerykańskim
#     match = date_pattern.search(file_name)
    
#     if match:
#         # Pobranie poszczególnych elementów daty
#         month = match.group(2)
#         day = match.group(3)
#         year = match.group(4)
        
#         # Utworzenie nowej nazwy pliku w stylu europejskim
#         new_file_name = match.group(1) + day + '-' + month + '-' + year + match.group(5)
        
#         # Zmiana nazwy pliku za pomocą funkcji shutil.move()
#         shutil.move(file_name, new_file_name)