#!python

#Three functions for this exercise. First, write a writeToFile() 
# function with two parameters for the filename of the file and the text
# to write into the file. 
# Second, write an appendToFile() function, which is identical to 
# writeToFile() except that the file opens in append mode instead
# of write mode. 
# Finally, 
# write a readFromFile() function with one parameter for the filename
# to open.This function returns the full text contents of the file 
# as a string.

def writeToFile(filename, text):
    # Open the file in write mode:
    with open(filename, 'w') as fileObj:
        # Write the text to the file:
        fileObj.write(text)

def appendToFile(filename, text):
    # Open the file in append mode:
    with open(filename, 'a') as fileObj:
        # Write the text to the end of the file:
        fileObj.write(text)

def readFromFile(filename):
    # Open the file in read mode:
    with open(filename) as fileObj:
        # Read all of the text in the file and return it as a string:
        return fileObj.read()

writeToFile('greet.txt', 'Hello!\n')
appendToFile('greet.txt', 'Goodbye!\n')

#Asseration
assert readFromFile('greet.txt') == 'Hello!\nGoodbye!\n'
print(f'all tests passed')