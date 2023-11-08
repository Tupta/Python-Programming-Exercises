x = 5
print(x)
y = 1
d = 1
while y <= x:
    print(y)
    y = y+1
    d = d+1
    print (d)

UC = -1

while UC != 5:
    print("1. Pokaż zadania")
    print("2. Dodaj zadania")
    print("3. Usuń zadanie")
    print("4. Zapisz zmiany do pliku")
    print("5. Wyjdź")

    US = int(input("Wybierz liczbę:    ") )