#!python

#makeChange() function with an amount parameter. 
# The amount parameter contains an integer of 
# the number of cents to make change for. 
# For example, 30 would represent 30 cents 
# and 125 would represent $1.25. This function 
# should return a dictionary with keys 'quarters', 
# 'dimes', 'nickels', and 'pennies', where the 
# value for a key is an integer of the number 
# of this type of coin.

def makeChange(amount):
    # Create a dictionary to keep track of how many of each coin:
    change = {}
    # If the amount is enough to add quarters, add them:
    if amount >= 25:
        change['quarters'] = amount // 25
        # Reduce the amount by the value of the quarters added:
        amount = amount % 25
    # If the amount is enough to add dimes, add them:
    if amount >= 10:
        change['dimes'] = amount // 10
        # Reduce the amount by the value of the dimes added:
        amount = amount % 10
    # If the amount is enough to add nickels, add them:
    if amount >= 5:
        change['nickels'] = amount // 5
        # Reduce the amount by the value of the nickels added:
        amount = amount % 5
    # If the amount is enough to add pennies, add them:
    if amount >= 1:
        change['pennies'] = amount
    return change


#aSSERATION
assert makeChange(30) == {'quarters': 1, 'nickels': 1}
assert makeChange(10) == {'dimes': 1}
assert makeChange(57) == {'quarters': 2, 'nickels': 1, 'pennies': 2}
assert makeChange(100) == {'quarters': 4}
assert makeChange(125) == {'quarters': 5}
print('all tests passed')