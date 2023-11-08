x = int(input("podaj dolny zakres liczby: "))
y = int(input("podaj górny zakres liczby: "))
skok = int(input ("podaj skok liczby: "))

for i in range(x, y, skok):
    print(i)
