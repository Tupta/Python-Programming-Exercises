#!python

# This function getSmallest() that has a numbers parameter. 
# The numbers parameter will be a list of integer 
# and floating-point number values. 
# The function returns the smallest value in the list. 
# If the list is empty, the function should return None. 
# Since this function replicates Python’s min() function, 
# your solution shouldn’t use it.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def getSmallest(numbers):
    
    # return None if list of numbers is empty
    if len(numbers) == 0:
        return None
   # Initialize the smallest number with the first element of the list
    min_value = numbers[0]
   
    # Iterate over the list starting from the second element
    for number in numbers[1:]:
        if number < min_value:
            min_value = number
    
    return min_value


# test one
numbers = [5, 3, 8, 1, 2]
print(getSmallest(numbers))  # Powinno zwrócić 1

# second test with empty list
empty_list = []
print(getSmallest(empty_list))  # Powinno zwrócić None        
    
#asseration

assert getSmallest([1, 2, 3]) == 1
assert getSmallest([3, 2, 1]) == 1
assert getSmallest([28, 25, 42, 2, 28]) == 2
assert getSmallest([1]) == 1
assert getSmallest([]) == None

print('all tests passed')