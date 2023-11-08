import os
x=os.path.join('usr','bin','spam')  #wstawianie slaszy do ścieżki katalogu
print(x)

y=os.getcwd()  #pobieranie ściezki katalogu roboczego
print(y)

#os.makedirs('c:\\delicious\\walnut\\waffles')  #tworzenie katalogu

d = os.path.dirname('c:\delicious\walnut\waffles')
print(d)

d1 = os.path.basename('c:\delicious\walnut\waffles')
print(d1)

# calcFilePath = 'C:\\Windows\\System32\\calc.exe'

# y1 = os.path.split(calcFilePath)
# print(y1)

d1 = os.path.getsize('C:\\Windows\\System32\\calc.exe')
print(d1)

totalSize = 0
for filename in os.listdir('C:\\Windows\\System32'):
    totalSize = totalSize + os.path.getsize(os.path.join('C:\\Windows\\System32', filename))
print(totalSize)
os.path.exists('C:\\Windows')

helloFile = open('C:\\Users\\sendrat\\Documents\\1.txt')

odczytpliku = helloFile.read()
print(odczytpliku)

totalSize = 0
for filename in os.listdir('C:\\Windows\\System32'):
    totalSize = totalSize + os.path.getsize(os.path.join('C:\\Windows\\System32', filename))
print(totalSize)

dsc = os.path.exists('D:\\')   # Sprawdzenie czy istnieje taki dysk/plik lub inne to co jest w ścieżce
print(dsc)