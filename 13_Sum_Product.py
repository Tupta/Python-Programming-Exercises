#!python

#two functions named calculateSum() and calculateProduct(). 
# They both have a parameter named numbers, which will be 
# a list of integer or floating-point values. 
# The calculateSum() function adds these numbers and returns 
# the sum while the calculateProduct() function multiplies these
# numbers and returns the product. 
# If the list passed to calculateSum() is empty, the function returns 0. 
# If the list passed to calculateProduct() is empty, the function returns 1. 
# Since this function replicates Python’s sum() function,your solution shouldn’t call.

numbers = [1, 2, 3]

def calculateSum(numbers):
    sum = 0
    for number in numbers:
        sum += number
    return sum

#print(calculateSum(numbers))

def calculateProduct(numbers):
    product = 1
    for number in numbers:
        product = product * number #(or product *= number) )
    return product

#print(calculateProduct(numbers))

#asseration
assert calculateSum([]) == 0
assert calculateSum([2, 4, 6, 8, 10]) == 30
assert calculateProduct([]) == 1
assert calculateProduct([2, 4, 6, 8, 10]) == 3840

print("all tests passed")