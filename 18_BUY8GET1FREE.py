#!python

# Function named getCostOfCoffee() that 
# has a parameters named numberOfCoffees 
# and pricePerCoffee. Given this information, 
# the function returns the total cost of the coffee order. 
# This is not a simple multiplication of cost and quantity, 
# however, because the coffee  shop has an offer 
# where you get one free coffee for every eight coffees you buy.

def getCostOfCoffee(numberOfCoffees, pricePerCoffee):
    # Get the total price for all coffees
    total_price = numberOfCoffees * pricePerCoffee
    
    # Get the free coffes number and discount for them
    
    free_coffee_number = numberOfCoffees // 9
    discount = free_coffee_number * pricePerCoffee
    
    #get the finally total price
    finally_price = total_price - discount

    return finally_price

#Asseration

assert getCostOfCoffee(7, 2.50) == 17.50
assert getCostOfCoffee(8, 2.50) == 20
assert getCostOfCoffee(9, 2.50) == 20
assert getCostOfCoffee(10, 2.50) == 22.50

for i in range(1, 4):
    assert getCostOfCoffee(0, i) == 0
    assert getCostOfCoffee(8, i) == 8 * i
    assert getCostOfCoffee(9, i) == 8 * i
    assert getCostOfCoffee(18, i) == 16 * i
    assert getCostOfCoffee(19, i) == 17 * i
    assert getCostOfCoffee(30, i) == 27 * i
print('all tests passed')