#!python

#drawPyramid() function with a height parameter. 
# The top of the pyramid has one centered hashtag 
# character, and the subsequent rows have two more 
# hashtags than the previous row. 
# The number of rows matches the height integer. 

def drawPyramid(height):
    # Loop over each row from 0 up to height:
    for rowNumber in range(height):
        # Create a string of spaces for the left side of the pyramid:
        leftSideSpaces = ' ' * (height - (rowNumber + 1))
        # Create the string of hashtags for this row of the pyramid:
        pyramidRow = '#' * (rowNumber * 2 + 1)
        # Print the left side spaces and the row of the pyramid:
        print(leftSideSpaces + pyramidRow)

#Asseeration
drawPyramid(5)
drawPyramid(15)
print(f'If You see pyramids everything is ok')