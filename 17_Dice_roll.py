#!python

# RollDice() function with a numberOfDice parameter 
# that represents the number of six-sided dice. 
# The function returns the sum of all of the dice rolls

import random
def rollDice(number):
    #starting sum = 0
    total = 0
    # Run a loop 
    for i in range(number):
        total += random.randint(1,6)
    
    # Return the dice roll total:  
    return total
    
#asseration
assert rollDice(0) == 0
assert rollDice(1000) != rollDice(1000)
for i in range(1000):
    assert 1 <= rollDice(1) <= 6
    assert 2 <= rollDice(2) <= 12
    assert 3 <= rollDice(3) <= 18
    assert 100 <= rollDice(100) <= 600
print('all tests passed')

##SECOND VERSION WITH RANDOM.CHOICE

# def rollDice(number):
#     # List of possible die faces
#     die_faces = [1, 2, 3, 4, 5, 6]
#     #starting sum = 0
#     total = 0
#     for i in range(number):
#         total += random.choice(die_faces)
#     return total  # Przeniesienie return na zewnątrz pętli
    
# # Asseration
# assert rollDice(0) == 0
# assert rollDice(1000) != rollDice(1000)
# for i in range(1000):
#     assert 1 <= rollDice(1) <= 6
#     assert 2 <= rollDice(2) <= 12
#     assert 3 <= rollDice(3) <= 18
#     assert 100 <= rollDice(100) <= 600

# print('all tests passed')