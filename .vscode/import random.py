import random, sys

for i in range(5):
    print(random.randint(1, 10))
    
while True:
    print ("wpisz exit, aby zakonczyć działanie programu.")
    response = input()
    if response == 'exit':
        sys.exit()