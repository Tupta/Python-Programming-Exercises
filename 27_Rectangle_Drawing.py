#!python

# drawRectangle() function with two integer parameters: 
# width and height. The function doesn’t return any 
# values but rather prints a rectangle with the given number
# of hashtags in the horizontal and vertical directions.


#definition
def drawRectangle(width, height):
    #main loop
    for i in range(height):
        print("#"*width)


#Asseration :D
drawRectangle(4,8)