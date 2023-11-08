
#!python

print("Ten program oblicza pole i obwód koła na podstawie podanego promienia\n")
r = float(input('Wprowadź wartość promienia koła:  '))
pi = 3.14

if r <= 0:
    print('Promień koła musi być liczbą oddatnią')
else:
    polekola = pi*float(r)**2
    obwkola = 2*pi*float(r)
    print("Pole koła o promieniu " +str(r) +"jest równe :" + str(polekola))
    print("Obwód koła o promieniu " +str(r) +"jest równe :" + str(obwkola))
    