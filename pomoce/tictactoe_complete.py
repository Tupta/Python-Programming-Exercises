# Gra w kółko i krzyżyk. Autor Al Sweigart al@inventwithpython.com
# To jest klasyczna gra planszowa.

ALL_SPACES = list('123456789')  # Klucze słownika przedstawiającego planszę do gry w kółko i krzyżyk.
X, O, BLANK = 'X', 'O', ' '  # Stałe wartości w postaci ciągów tekstowych.

def main():
    """Uruchamia grę w kółko i krzyżyk."""
    print('Witaj w grze w kółko i krzyżyk!')
    gameBoard = getBlankBoard()  # Utworzenie słownika przedstawiającego planszę do gry w kółko i krzyżyk.
    currentPlayer, nextPlayer = X, O  # Najpierw gracz X, później gracz O.

    while True:
        print(getBoardStr(gameBoard))  # Wyświetlenie planszy na ekranie.

        # Pytanie będzie wyświetlane dopóty, dopóki gracz nie wpisze cyfry 1-9.
        move = None
        while not isValidSpace(gameBoard, move):
            print('Jaki ruch gracza {}? (1-9)'.format(currentPlayer))
            move = input()
        updateBoard(gameBoard, move, currentPlayer)  # Wykonanie ruchu.

        # Sprawdzenie, czy nastąpił koniec gry.
        if isWinner(gameBoard, currentPlayer):  # Najpierw sprawdzenie pod kątem wygranej.
            print(getBoardStr(gameBoard))
            print('Wygrał gracz' + currentPlayer + '!')
            break
        elif isBoardFull(gameBoard):  # Następnie sprawdzenie pod kątem remisu.
            print(getBoardStr(gameBoard))
            print('Mamy remis!')
            break
        currentPlayer, nextPlayer = nextPlayer, currentPlayer  # Zmiana gracza wykonującego ruch.
    print('Dziękuję za udział w grze!')

def getBlankBoard():
    """Utworzenie nowej, pustej planszy do gry w kółko i krzyżyk."""
    board = {}  # Planszę przedstawia słownik Pythona.
    for space in ALL_SPACES:
        board[space] = BLANK  # Na początku wszystkie pola są puste.
    return board

def getBoardStr(board):
    """Zwrot planszy w postaci tekstowej."""
    return '''
      {}|{}|{}  1 2 3
      -+-+-
      {}|{}|{}  4 5 6
      -+-+-
      {}|{}|{}  7 8 9'''.format(board['1'], board['2'], board['3'], board['4'], board['5'], board['6'], board['7'], board['8'], board['9'])

def isValidSpace(board, space):
    """Zwrot wartości True, jeżeli podano numer pola
    oraz jeżeli podane pole jest puste."""
    return space in ALL_SPACES and board[space] == BLANK

def isWinner(board, player):
    """Zwrot wartości True, jeżeli tę rundę wygrał gracz."""
    b, p = board, player  # Krótsze nazwy dla planszy i gracza.
    # Sprawdzenie pod kątem trzech znaków w rzędzie, kolumnie lub na ukos.
    return ((b['1'] == b['2'] == b['3'] == p) or  # Wiersz na górze.
            (b['4'] == b['5'] == b['6'] == p) or  # Wiersz na pośrodku.
            (b['7'] == b['8'] == b['9'] == p) or  # Wiersz na dole.
            (b['1'] == b['4'] == b['7'] == p) or  # Kolumna po lewej.
            (b['2'] == b['5'] == b['8'] == p) or  # Kolumna pośrodku.
            (b['3'] == b['6'] == b['9'] == p) or  # Kolumna po prawej.
            (b['3'] == b['5'] == b['7'] == p) or  # Po przekątnej.
            (b['1'] == b['5'] == b['9'] == p))    # Po przekątnej.

def isBoardFull(board):
    """Zwrot wartości True, jeżeli wszystkie pola na planszy są wypełnione."""
    for space in ALL_SPACES:
        if board[space] == BLANK:
            return False  # Jeżeli pozostało jedno puste pole, wartością zwrotną jest False.
    return True  # Brak pustych pól, więc wartością zwrotną jest True.

def updateBoard(board, space, mark):
    """Umieszczenie znaku w polu na planszy."""
    board[space] = mark

if __name__ == '__main__':
    main()  # Wywołanie funkcji main(), jeżeli moduł został uruchomiony oddzielnie, a nie zaimportowany w innym programie.
