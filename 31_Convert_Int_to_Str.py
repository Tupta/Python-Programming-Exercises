#!python

# Convert Integers to Strings
#convertIntToStr() function with an integerNum parameter. 
# This function operates similarly to the str() function in 
# that it returns a string form of the parameter


def convertIntToStr(integerNum):
    # Special case: Check if integerNum is 0, and return '0' if so:
    if integerNum == 0:
        return '0'

    # This dictionary maps single integer digits to string digits:
    DIGITS_INT_TO_STR = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4',
                         5: '5', 6: '6', 7: '7', 8: '8', 9: '9'}

    # Make a note whether the number is negative or not, and make
    # integerNum positive for the rest of the function's code:
    if integerNum < 0:
        isNegative = True
        integerNum = -integerNum
    else:
        isNegative = False

    # stringNum holds the converted string, and starts off blank:
    stringNum = ''

    # Keeping looping while integerNum is greater than zero:
    while integerNum > 0:
        # Mod the integerNum by 10 to get the digit in the ones place:
        onesPlaceDigit = integerNum % 10
        # Put the corresponding string digit at the front of stringNum:
        stringNum = DIGITS_INT_TO_STR[onesPlaceDigit] + stringNum
        # Divide integerNum by ten to remove one entire digit place:
        integerNum //= 10

    # If the number was originally negative, add a minus sign:
    if isNegative:
        return '-' + stringNum
    else:
        return stringNum


# Assertion tests
assert convertIntToStr(0) == '0'
assert convertIntToStr(123) == '123'
assert convertIntToStr(-456) == '-456'

print("All tests passed")

