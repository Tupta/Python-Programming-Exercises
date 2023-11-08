kraje_i_stolice = {"Polska" : "Warszawa", "Niemcy" : "Berlin", "Hiszpania" : "Madryt" }
print (kraje_i_stolice)
print()
print()
kraje_i_stolice['Boliwia'] = "Bogota"
print (kraje_i_stolice)

for kraje in kraje_i_stolice.keys():
    print(kraje)
##### KRAJE SĄ KLUCZAMI
print()
print()
for stolice in kraje_i_stolice.values():
    print(stolice)
##### STOLICE SĄ WARTOŚCIAMI

for kraje, stolice in kraje_i_stolice.items():
    print(kraje + "-" + stolice)

print()
print()
print()
print(kraje_i_stolice["Boliwia"])
print(kraje_i_stolice.get("Boliwia"))