import time

def calcProd():
# Funkcja oblicza iloczyn pierwszych 100 000 liczb.
    product = 1
    for i in range(1, 100000):
        product = product * i
    return product

startTime = time.time()
prod = calcProd()
endTime = time.time()
print('Wynik składa się z %s cyfr.' % (len(str(prod))))
print('Wykonanie kodu zabrało %s sekund.' % (endTime - startTime))