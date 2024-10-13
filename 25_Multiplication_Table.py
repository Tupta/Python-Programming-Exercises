#!python

# Print the heading of each column that will be always the same:
print('  | 1  2  3  4  5  6  7  8  9 10')
print('--+------------------------------')


# loop throug all numbers from 1 to 10
for column in range(1, 11):
    # number label on the right side:
    print(str(column).rjust(2) + '|', end='')
    
    #now it's time for a loop over all numbers 1 to 10:
    for row in range(1, 11):
        print(str(row * column).rjust(2) + ' ', end='')
    #After the loop print a new line to end the row
    print() 