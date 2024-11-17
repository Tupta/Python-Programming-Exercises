#!python


# shuffle() function with a values parameter set to a list of values. 
# The function doesn’t return anything, but rather it sets each value in the list to a random index. 
# The resulting shuffled list must contain the 
# same values as before but in random order.

# Import the random module for its randint() function.
import random
def shuffle(values):
    # Loop over the range of indexes from 0 up to the length of the list:
    for i in range(len(values)):
        # Randomly pick an index to swap with:
        swapIndex = random.randint(0, len(values) - 1)
        # Swap the values between the two indexes:
        values[i], values[swapIndex] = values[swapIndex], values[i]

#Asseration
# 
random.seed(42)

# Perform this test ten times:

for i in range(10):

    testData1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    shuffle(testData1)

    # Make sure the number of values hasn't changed:

    assert len(testData1) == 10

    # Make sure the order has changed:

    assert testData1 != [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # Make sure that when re-sorted, all the original values are there:

    assert sorted(testData1) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

 

# Make sure an empty list shuffled remains empty:

testData2 = []

shuffle(testData2)

assert testData2 == []        
print('all tests passed')