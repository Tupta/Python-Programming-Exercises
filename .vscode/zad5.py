
#!python3

# Napisz program, który znajdzie największy, najmniejszy element  oraz średnią arytmetyczną listy liczb. 
# Możesz to zrobić wykorzystując pętle for lub znaleźć odpowiednie do tego działania funkcje. Powodzenia!


try:
    liczby = input("Podaj listę liczb, oddzielając je przecinkami: ").split(',')
    print("Oto twoje liczby : ", liczby)
    liczby = [float(x) for x in liczby]  # Konwersja na liczby zmiennoprzecinkowe
except ValueError:
     print("Podano niepoprawne liczby.")
     exit()

if len(liczby) == 0:
    print("Lista jest pusta. Nie można obliczyć wartości.")
    exit()

# Znajdź największy i najmniejszy element
najwiekszy = max(liczby)
najmniejszy = min(liczby)

# Oblicz średnią arytmetyczną
srednia = sum(liczby) / len(liczby)

# Wyświetl wyniki
print(f"Największy element: {najwiekszy}")
print(f"Najmniejszy element: {najmniejszy}")
print(f"Średnia arytmetyczna: {srednia}")