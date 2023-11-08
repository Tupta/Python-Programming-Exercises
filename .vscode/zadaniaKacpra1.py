#!python3


# Zadanie 1

# Napisz program, który odbierze długości dwóch boków(przyprostokątnych) trójkąta prostokątnego. 
# Twoim zadaniem jest skorzystanie z twierdzenia pitagorasa i policzenie długości trzeciego boku trójkąta(przeciwprostokątnej).

# import math

# a = float(input("podaj długość pierwszej przyprostokątnej: "))

# b = float(input("podaj długość drugiej przyprostokątnej: "))

# c= math.sqrt(a*a+b*b)

# print(f' długość przyprostokątnej = {c}')

###############################################


# Zadanie 2

# Przygotuj program, który zapyta użytkownika:
# "Aby zamienić stopnie Celsjusza na Fahrenheity napisz 1, aby dokonać odwrotnej zamiany napisz 2", 
# a następnie zapytaj go o wartość do zamiany. W odpowiedzi program powinien wyświetlić prawidłowy wynik.

# Temp = float(input('podaj temperature jaką chcesz przeliczyć: '))

# print("Jeżeli podałeś w temp w stopniach Celcjusza i chcesz przeliczyć ją na stopnie fahrenheita naciśnij 1.\n\nJeżeli podałeś temp w sopniach farenheitha i ches zprzeliczyć ją na stopnie celcjusza naciśnij 2")

# choice = int(input("wybierz na co przeliczamy podana temp: "))

# if choice == 1:
#     finalTemp = 2 * Temp + 32
#     print(f' Temperatura wynosi {finalTemp} stopni fahrenheita')
# elif choice == 2:
#     finalTemp = (Temp - 30)/2
#     print(f' Temperatura wynosi {finalTemp} stopni celcjusza')
# else:
#     print('dokonałeś złego wyboryu jeszcze raz')


# Zadanie 3

# Odbierz od użytkownika dwa dowolne punkty na płaszczyźnie(x1, y1, x2, y2), które tworzą odcinek. 
# Musisz zapytać użytkownika o cztery wartości. Napisz jakie jest pole oraz promień okręgu, którego ten odcinek jest średnicą. 
# Dla ułatwienia przyjmij, że PI ma wartość 3.14. 

import math

x1, y1, x2, y2 = map(float, input("Podaj współrzędne dwóch punktów oddzielone przecinkiem (x1, y1, x2, y2): ").split(","))

# Point_A = float(input("podaj współrzędne pierwszego odcinak odzielając je przecinkiem: "))
# Point_B = float(input("podaj współrzędne pierwszego odcinak odzielając je przecinkiem: "))
#Odcinek = math.sqrt((Point_B[0]-Point_A[0])**2 + (Point_B[1]-Point_A[1])**2)

Diameter = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print(Diameter)

Circle_radius = Diameter/2

Circle_Area = 2*3.14*(Circle_radius)**2

print(f'długośc promienia koła opisanego na tych dwóch punktach wynosi {Circle_radius} , natomiast jego pole jest równe: {Circle_Area} ')