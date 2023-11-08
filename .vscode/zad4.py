#!python3

# # Zadanie 4
# Odbierz od użytkownika liczbę, a następnie policz sumę wszystkich liczb parzystych od 0 do tej liczby(włącznie). 
# Dla przykładu, jeżeli użytkownik poda nam liczbę 10 to powinniśmy policzyć sumę 2 + 4 + 6 + 8 + 10 = 30

x = d = int(input('podaj liczbe:   '))

sum = 0

if x % 2 != 0:
    x -= 1
    
for i in range(0, x+1, 2):
    sum += i

print(sum)
print("Suma liczb parzystych od 0 do", d, "i liczby", d , "wynosi: ", sum)