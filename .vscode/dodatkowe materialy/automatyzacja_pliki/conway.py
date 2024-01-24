# Gra w życie Johna Conwaya.
import random, time, copy
WIDTH = 60
HEIGHT = 20

# Utworzenie listy list przedstawiającej komórki.
nextCells = []
for x in range(WIDTH):
    column = []  # Utworzenie nowej kolumny.
    for y in range(HEIGHT):
        if random.randint(0, 1) == 0:
            column.append('#')  # Dodanie komórki żywej.
        else:
            column.append(' ')  # Dodanie komórki martwej.
    nextCells.append(column)  # nextCells to lista list kolumn.

while True:  # Pętla główna programu
    print('\n\n\n\n\n')  # Oddzielenie poszczególnych kroków znakami nowego wiersza.
    currentCells = copy.deepcopy(nextCells)

    # Wyświetlenie currentCells na ekranie.
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(currentCells[x][y], end='')  # Wyświetlenie znaku # lub spacji.
        print()  # Wyświetlenie znaku nowego wiersza na końcu danego wiersza komórek.

    # Obliczenie komórek w następnym kroku na podstawie komórek bieżącego kroku.
    for x in range(WIDTH):
        for y in range(HEIGHT):
            # Pobranie współrzędnych komórek sąsiadujących z daną komórką.
            # `% WIDTH` gwarantuje, że wartość leftCoord zawdze będzie w przedziale od 0 do WIDTH - 1.
            leftCoord  = (x - 1) % WIDTH
            rightCoord = (x + 1) % WIDTH
            aboveCoord = (y - 1) % HEIGHT
            belowCoord = (y + 1) % HEIGHT

            # Liczba sąsiadujących żywych komórek.
            numNeighbors = 0
            if currentCells[leftCoord][aboveCoord] == '#':
                numNeighbors += 1  # Sąsiadująca komórka w lewym górnym rogu jest żywa.
            if currentCells[x][aboveCoord] == '#':
                numNeighbors += 1  # Sąsiadująca komórka na górze jest żywa.
            if currentCells[rightCoord][aboveCoord] == '#':
                numNeighbors += 1  # Sąsiadująca komórka w prawym górnym rogu jest żywa.
            if currentCells[leftCoord][y] == '#':
                numNeighbors += 1  # Sąsiadująca komórka po lewej stronie jest żywa.
            if currentCells[rightCoord][y] == '#':
                numNeighbors += 1  # Sąsiadująca komórka po prawej stronie jest żywa.
            if currentCells[leftCoord][belowCoord] == '#':
                numNeighbors += 1  # Sąsiadująca komórka w lewym dolnym rogu jest żywa.
            if currentCells[x][belowCoord] == '#':
                numNeighbors += 1  # Sąsiadująca komórka na dole jest żywa.
            if currentCells[rightCoord][belowCoord] == '#':
                numNeighbors += 1  # Sąsiadująca komórka w prawym dolnym rogu jest żywa.

            # Określenie stanu komórki na podstawie reguł gry w życie Johna Conwaya.
            if currentCells[x][y] == '#' and (numNeighbors == 2 or numNeighbors == 3):
                # Dwie lub trzy żywe komórki sąsiadujące, oznaczają, że komórka pozostaje żywa.
                nextCells[x][y] = '#'
            elif currentCells[x][y] == ' ' and numNeighbors == 3:
                # Trzy żywe komórki sąsiadujące, oznaczają, że komórka ożywa.
                nextCells[x][y] = '#'
            else:
                # Reszta komórek pozostaje martwa lub obumiera.
                nextCells[x][y] = ' '
    time.sleep(1)  # Dodanie sekundowej przerwy, aby zminimalizować miganie ekranu.
