#!python

#This program prints a multiplication table on the screen 
# using nested for loops and some string manipulation to 
# align the columns correctly.

# Loop over all numbers from 1 to 10:

for column in range(1, 11):

    # Print the number label on the right side remeber to put endswitch:

    print(str(column).rjust(2) + '|', end=' ')

    # Loop over all numbers from 1 to 10:

    for row in range(1, 11):

        # Print the product, padded to two digits, followed by a space rjust(3) is importand:

        print(str(row*column).rjust(3) + ' ', end=' ')

    # After the loop, print a newline to end the row:

    print()