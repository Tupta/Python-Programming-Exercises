file = open("kraje_i_stolice.txt", "w+")

kraje = {'polska': "Wawa", "włochy" : "Rzym", "Estonia" : "Talin", "Dania" : "Kopenhaga"}


for kraje, stolice in kraje.items():
    file.write(kraje + "-" + stolice + "\n")

file.close()


###### ponizej odczyt pliku
file = open("kraje_i_stolice.txt")

for linia in file.readlines():
    print(linia)

####### żeby nie było wolnych linii pomiędzy poszczególnymi wierszami należy w powyuższym poleceniu uzyć strip'a w taki psosób:::::  "print(linia.strip())""
