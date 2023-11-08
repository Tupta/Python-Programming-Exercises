inventory = {'lina': 1, 'pochodnia': 6, 'złote monety': 42, 'sztylet': 1,'strzała': 12}
# x = sum(inventory.values())
# print('całkowita liczba przedmiotów: ' + str(x))

def displayInventory():
    print('Inwentarz:')
    for k, v in inventory.items():
        print(str(v) + ' - ' + k)
    x = sum(inventory.values())
    print('Całkowita liczba przedmiotów: ' + str(x))

displayInventory()



# Utwórz funkcję o nazwie displayInventory(), za pomocą której
# będzie możliwe sporządzenie „inwentarza” i jego
# wyświetlenie tak, jak pokazałem poniżej.
# Inwentarz:
# 12 strzał
# 42 złote monety
# 1 lina
# 6 pochodni
# 1 sztylet
# Całkowita liczba przedmiotów: 62