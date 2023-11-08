
import shutil, os
os.chdir('C:\\')
shutil.copy('C:\\spam.txt', 'C:\\delicious')

shutil.copy('eggs.txt', 'C:\\delicious\\eggs2.txt')


# Pierwsze wywołanie shutil.copy() kopiuje plik C:\spam.txt do
# katalogu C:\delicious. Wartością zwrotną jest ścieżka
# dostępu do nowo skopiowanego pliku. Zwróć uwagę na
# fakt, że ponieważ katalog został wskazany jako docelowa
# ścieżka dostępu , więc oryginalna nazwa pliku spam.txt
# będzie zachowana dla nowo skopiowanego pliku. Drugie
# wywołanie shutil.copy() w wierszu powoduje skopiowanie
# pliku C:\eggs.txt do katalogu C:\delicious, ale nowo
# skopiowanemu plikowi nadaje nazwę eggs2.txt.

shutil.copytree('C:\\bacon', 'C:\\bacon_backup')

# W omawianym przykładzie wywołanie funkcji
# shutil.copytree() spowoduje utworzenie katalogu o nazwie
# bacon_backup wraz z zawartością taką samą jak zawartość
# katalogu źródłowego bacon. W ten sposób utworzyłeś kopię
# zapasową cennego katalogu.