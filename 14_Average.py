#!python

# An average() function that has a numbers 
# parameter. This function returns the statistical 
# average of the list of integer and floating-point 
# numbers passed to the function. 
# Without Python’s built-in sum() function

def average(numbers):
    
    d=len(numbers)
    if d == 0: 
        return 0.0
    sum = 0.0
    for i in numbers:
        sum += i
    average = sum/d
    return average


assert average([1, 2, 3]) == 2
assert average([1, 2, 3, 1, 2, 3, 1, 2, 3]) == 2
assert average([12, 20, 37]) == 23
assert average([0, 0, 0, 0, 0]) == 0
import random
random.seed(42)
testData = [1, 2, 3, 1, 2, 3, 1, 2, 3]
for i in range(1000):
    random.shuffle(testData)
    assert average(testData) == 2
print('ALL TEST PASS')