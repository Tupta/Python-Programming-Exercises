#!python

# drawBorder() function with parameters width and height. 
# The function draws the border of a rectangle with the 
# given integer sizes. There are no 
# Python assert statements to check the correctness of 
# your program. Instead, you can visually inspect the 
# output yourself. For example, calling drawBorder(16, 4) 
# would output the following:

# +--------------+
# |              |
# |              |
# +--------------+

#The interior of the rectangle requires printing spaces.
# The sizes given include the space required for the 
# corners. If the width or height parameter is less than 
# 2, the function should print nothing.


def drawBorder(width, height):

    # Special case: If the width or height is less than two, draw nothing:
    if width < 2 or height < 2:
        return
     # Print the top row:
    print('+' + ('-' * (width - 2)) + '+')
     # Loop for each row (except the top and bottom):
    for i in range(height - 2):
        # Print the sides:
        print('|' + (" " * (width - 2)) + '|')

    # Print the bottom row:
    print('+' + ('-' * (width - 2)) + '+')
        # def drawRectangle(width, height):
            
#Asseration :D
drawBorder(16,4)
drawBorder(20,10)
