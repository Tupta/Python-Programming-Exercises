#!python

#function named collatz() with a startingNumber parameter. 
# The function returns a list of integers of the Collatz 
# sequence that startingNumber produces

def collatz(startingNumber):
    # If the starting number is 0 or negative, return an empty list:
    if startingNumber < 1:
        return []
    # Create a list to hold the sequence, beginning with the starting number:
    sequence = [startingNumber]
    num = startingNumber
    # Keep looping until the current number is 1:
    while num != 1:
        # If odd, the next number is 3 times the current number plus 1:
        if num % 2 == 1:
            num = 3 * num + 1
        # If even, the next number is half the current number:
        else:
            num = num // 2
            # Record the number in the sequence list:
        sequence.append(num)
    # Return the sequence of numbers:
    return sequence


#ASSERATION

assert collatz(0) == []
assert collatz(10) == [10, 5, 16, 8, 4, 2, 1]
assert collatz(11) == [11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
assert collatz(12) == [12, 6, 3, 10, 5, 16, 8, 4, 2, 1]
assert len(collatz(256)) == 9
assert len(collatz(257)) == 123
print('all tests passed')
import random

random.seed(42)

for i in range(1000):
    startingNum = random.randint(1, 10000)
    seq = collatz(startingNum)
    assert seq[0] == startingNum # Make sure it includes the starting number.
    assert seq[-1] == 1  # Make sure the last integer is 1.
   