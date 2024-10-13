Python Programming Exercises, Gently Explained
145
for i in range(height - 2):
# Print the sides:
print('|' + (' ' * (width - 2)) + '|')
# Print the bottom row:
print('+' + ('-' * (width - 2)) + '+')
Exercise #29: Pyramid Drawing
def drawPyramid(height):
# Loop over each row from 0 up to height:
for rowNumber in range(height):
# Create a string of spaces for the left side of the pyramid:
leftSideSpaces = ' ' * (height - (rowNumber + 1))
# Create the string of hashtags for this row of the pyramid:
pyramidRow = '#' * (rowNumber * 2 + 1)
# Print the left side spaces and the row of the pyramid:
print(leftSideSpaces + pyramidRow)
Exercise #30: 3D Box Drawing
def drawBox(size):
# Special case: Draw nothing if size is less than 1:
if size < 1:
return
# Draw back line on top surface:
print(' ' * (size + 1) + '+' + '-' * (size * 2) + '+')
# Draw top surface:
for i in range(size):
print(' ' * (size - i) + '/' + ' ' * (size * 2) + '/' + ' ' * i + '|')
# Draw top line on top surface:
print('+' + '-' * (size * 2) + '+' + ' ' * size + '+')
# Draw front surface:
for i in range(size - 1, -1, -1):
print('|' + ' ' * (size * 2) + '|' + ' ' * i + '/')
# Draw bottom lie on front surface:
print('+' + '-' * (size * 2) + '+')
# In a loop, call drawBox() with arguments 1 to 5:
for i in range(1, 6):
drawBox(i)
Exercise #31: Convert Integers to Strings
def convertIntToStr(integerNum):
# Special case: Check if integerNum is 0, and return '0' if so:
if integerNum == 0:
return '0'
Python Programming Exercises, Gently Explained
146
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