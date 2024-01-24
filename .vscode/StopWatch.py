# stopwatch.py — Prosty program stopera.



#! python3

import time

# Wyświetlenie informacji o sposobie działania programu.
print('\nNaciśnij Enter, aby rozpocząć. Kolejne naciśnięcie Enter, oznacza nowe okrążenie.\nlub\nNaciśnięcie Ctrl+C kończy działanie programu.')
input() # Naciśnij Enter, aby rozpocząć.
print('Rozpoczęto działanie.')
startTime = time.time() # Pobranie godziny rozpoczęcia pierwszego okrążenia.
lastTime = startTime
lapNum = 1
# TODO: Rozpoczęcie pomiaru czasu okrążenia.

