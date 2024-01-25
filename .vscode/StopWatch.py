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

try:
    while True:
        input()
        laptime = round(time.time() - lastTime, 2)
        totalTime = round(time.time() - startTime, 2)
        print ('okrążenie #%s: %s (%s)' % (lapNum, totalTime, laptime), end ='')

        lapNum +=1
        lastTime = time.time() #wyzeroweanie czasu ostatniego okrążenia

except KeyboardInterrupt:
   
    # Obsługa wyjątku zgłaszanego po naciśnięciu klawiszy Ctrl+C. Dzięki temu nie będzie wyswietlanego komunikatu błędu
    print('\nGotowe!')
    

