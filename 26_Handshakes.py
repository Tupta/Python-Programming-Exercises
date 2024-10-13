#!python.

#function named printHandshakes() with a list parameter named 
# people which will be a list of strings of people’s names. 
# The function prints out 'X shakes hands with Y', 
# where X and Y are every possible pair of handshakes between 
# the people in the list. No duplicates are permitted
#The printHandshakes() function must also return an integer 
# of the number of handshakes.


people=['Alice', 'Bob', 'Carol', 'David']
def printHandshakes(people):
    nohandshakes = 0
    i = len(people)
    #print(i)
    for i in range(0, i-1): #lopp  by index
        for j in range(i+1, len(people)): #lopp by next persons
            print(f'{people[i]} shakes hands with {people[j]}')
            #increment number of handshakes
            nohandshakes += 1
    #return number of handshakes
    print(f'Liczba wszystkich uściśnieć jest równa:{nohandshakes}')
printHandshakes(people)
 
