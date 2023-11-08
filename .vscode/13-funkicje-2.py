kraje = {}
kraje["Polska"] = ("Warszawa", 37.97, "wysocy")
kraje["Boliwia"] = ("Bogota", 56.77, "średni")
kraje["Anglia"] = ("Londyn", 17.22, "niscy")


##try:
##    print()
###except None:
##    print("takiego kraju nie ma na liście")
def pokaz_kraj(kraj):
    kraj = kraje.get(kraj)    ###### Tutaj porownujemy wprowadzoną zmienna "kraj" z zasobami naszego słownika. Jezeli wprowadzona przez uzytkownika zmienna "kraj"
### znajduje się w słowniku to pobierane są dla tego klucza/ wartości z krotki czyli stolica, ilosc ludnosci, itd... 
    print()
    print(kraj)
    print("---------------")
    print("Stolica: " + kraj[0])
    print("liczba mieszkańców: " + str(kraj[1]))
    print("ludzie w tym kraju ludzie są " + kraj[2] )

for kraj in kraje.keys():
    print(kraj)
print()
print()
kraj = input("Informacje o jakim kraju chcesz wyświelić?") #### Tutaj wprowadzamy naszą nową zmienna... uzytkownik ja wprowadza
pokaz_kraj(kraj)

print()
def wiadomosc():
    print("funkcja wyrzucania tekstu czy co tam chcesz")
wiadomosc()
