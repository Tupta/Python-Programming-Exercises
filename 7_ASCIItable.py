#!python

#ACIITable function display the ASCII number and its corresponding 
# text character, # from 32 to 126. 
# (These are called the printable ASCII characters.)

def printASCIITable():
    # Loop over integers 32 up to and including 126:
    for i in range(32, 127):
        # Print the integer and its ASCII text character:
        print(i, chr(i))

printASCIITable()
