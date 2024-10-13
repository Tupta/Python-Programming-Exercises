#!python

#drawBox() function with a size parameter. 
# The size parameter contains an integer for the width, 
# length, and height of the box. The horizontal lines 
# are drawn with - dash characters, the vertical lines 
# with | pipe characters, and the diagonal lines with / 
# forward slash characters. 
# The corners of the box are drawn with + plus signs.


def drawBox(size):
    # Special case: Draw nothing if size is less than 1:
    if size < 1:
        return
    
    # Draw the back line on the top surface:
    print(' ' * (size + 1) + '+' + '-' * (size * 2) + '+')
    
    # Draw the top surface (diagonal lines and right edge):
    for i in range(size):
        print(' ' * (size - i) + '/' + ' ' * (size * 2) + '/' + ' ' * i + '|')

    # Draw the front line on the top surface:
    print('+' + '-' * (size * 2) + '+' + ' ' * size + '+')

    # Draw the front surface (front vertical and right edge):
    for i in range(size - 1, -1, -1):
        print('|' + ' ' * (size * 2) + '|' + ' ' * i + '/')

    # Draw the bottom line of the front surface:
    print('+' + '-' * (size * 2) + '+')

#Asseration Test the function by calling drawBox():
drawBox(10)
drawBox(5)
drawBox(3)