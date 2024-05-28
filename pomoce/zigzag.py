import time, sys
indent = 0 # Wyrażona w spacjach wielkość wcięcia.
indentIncreasing = True # Określenie, czy wcięcie jest zwiększane, czy nie.

try:
    while True: # Pętla główna programu.
        print(' ' * indent, end='')
        print('********')
        time.sleep(0.1) # Wstrzymanie działania na 1/10 sekundy.

        if indentIncreasing:
            # Zwiększenie liczby spacji.
            indent = indent + 1
            if indent == 20:
                # Zmiana kierunku.
                indentIncreasing = False
        else:
            # Zmniejszenie liczby spacji.
            indent = indent - 1
            if indent == 0:
                # Zmiana kierunku.
                indentIncreasing = True
except KeyboardInterrupt:
    sys.exit()
