#!python


#Napisz program, który zapyta użytkownika jak ma na imię i jeśli to będzie Twoje imię to wypisze komunikat powitalny 
#np. "Cześć Kacper!" w przeciwnym razie powinien wyświetlić się komunikat np. "Alina! Miło mi Cię poznać!"

imie = input("Podaj swoje imię!!")

if imie.lower() == "tomasz":
    print("Cześć Tomasz!")
else:
    print(imie +"! Miło mi Cię poznać!")