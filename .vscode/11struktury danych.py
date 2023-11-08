######tworzenie listy

#lista_imion = []
#lista_imion.append("Piotrek")
#lista_imion.append("Tymek")
#lista_imion.append("Ania")

#print(lista_imion)


######sortowanie listy i inne sposoby jej wyswietlania

lista_imion = ["jacek", "ania", "piotrek", "tymek", "wojtek", "ania", "wojtek", "jurek", "stefan", "ania"]
print(lista_imion)

######albo inna możliwość wyswietlania zawartości listy czyli elementu listy pod elementem listy

#for imie in lista_imion:
    ######"imie" jest zmienna
#    print(imie)

######sortowanie listy
print("posortuje liste alfabetycznie")
lista_imion.sort()
print(lista_imion)

#####wyświetlanie konkretnego elementu listy

print("a teraz wyświetle tylko 4 imie na liście")
print(lista_imion[3])

print("policzymy teraz ile razy występuje imie ania na liście")
print("imie ania występuje na liscie", lista_imion.count("ania"), " razy")

print("dodatkowo powiem ci ile ejst wszystkich imion na liście")
print("wszystkich imion na liście jest", len(lista_imion))

lista_imion2 = ["daria", "magda", "jola", "gosia"]
print (lista_imion2)

lista_imion3 = lista_imion2 + lista_imion

print (lista_imion3)