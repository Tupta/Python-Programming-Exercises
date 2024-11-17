#!python

# mergeTwoLists() function with two parameters list1 and list2. 
# The lists of numbers passed for these parameters are already 
# in sorted order from smallest to largest number. 
# The function returns a single sorted list of all numbers 
# from these two lists.

def mergeTwoLists(list1, list2):
    # Create an empty list to hold the final sorted results:
    result = []
    # Start i1 and i2 at index 0, the start of list1 and list2:
    i1 = 0
    i2 = 0  
    # Keeping moving up i1 and i2 until one reaches the end of its list:
    while i1 < len(list1) and i2 < len(list2):
        # Add the smaller of the two current items to the result:
        if list1[i1] < list2[i2]:
            # Add list1's current item to the result:
            result.append(list1[i1])
            # Increment i1:
            i1 += 1
        else:
            # Add list2's current item to the result:
            result.append(list2[i2])
            # Increment i2:
            i2 += 1
            # If i1 is not at the end of list1, add the remaining items from list1:
    if i1 < len(list1):
        for j in range(i1, len(list1)):
            result.append(list1[j])
        # If i2 is not at the end of list2, add the remaining items from list2:
    if i2 < len(list2):
        for j in range(i2, len(list2)):
            result.append(list2[j])
    # Return the merged, sorted list:
    return result

#ASSERATION
assert mergeTwoLists([1, 3, 6], [5, 7, 8, 9]) == [1, 3, 5, 6, 7, 8, 9]
assert mergeTwoLists([1, 2, 3], [4, 5]) == [1, 2, 3, 4, 5]
assert mergeTwoLists([4, 5], [1, 2, 3]) == [1, 2, 3, 4, 5]
assert mergeTwoLists([2, 2, 2], [2, 2, 2]) == [2, 2, 2, 2, 2, 2]
assert mergeTwoLists([1, 2, 3], []) == [1, 2, 3]
assert mergeTwoLists([], [1, 2, 3]) == [1, 2, 3]
print ('all tests passed')