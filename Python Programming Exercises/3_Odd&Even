# Odd & Even

# Determining if a number is even or odd is a common calculation 
# that uses the modulo operator.

def isOdd(number):
    if not isinstance(number, int):
        return False
    return number % 2 != 0

def isEven(number):
    if not isinstance(number, int):
        return False
    return number % 2 == 0

# Testy asercji
assert isOdd(42) == False
assert isOdd(9999) == True
assert isOdd(-10) == False
assert isOdd(-11) == True
assert isOdd(3.1415) == False

assert isEven(42) == True
assert isEven(9999) == False
assert isEven(-10) == True
assert isEven(-11) == False
assert isEven(3.1415) == False

print("All tests passed!")
