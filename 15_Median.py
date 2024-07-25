#!python

#median() function that has a numbers 
# parameter. This function returns 
# the statistical median of the numbers 
# list. The median of an odd-length list 
# is the number in the middlemost number 
# when the list is in sorted order. 
# If the list has an even length, 
# the median is the average of the two 
# middlemost numbers when the list is in 
# sorted order. 

def median(numbers):
    # If the numbers list is empty, return None:
    if len(numbers) == 0:
        return None
    
    #sorting the lis
    sorted_List = sorted(numbers)
    #determining the number of numbers in the set
    n = len(sorted_List)
    #condition for odd list
    if n % 2 == 1:
        return sorted_List[n // 2]
    #condition for even list
    else:
        mid1 = sorted_List[n // 2 -1]
        mid2 = sorted_List[n // 2]
        return (mid1 + mid2) /2
        
#asseracja
assert median([1, 2, 3]) == 2
assert median([1, 2, 3, 4]) == 2.5
assert median([1, 3, 3, 6, 7, 8, 9]) == 6
assert median([1, 2, 3, 4, 5, 6, 8, 9]) == 4.5
assert median([]) == None

print("All tests passed") 
    
