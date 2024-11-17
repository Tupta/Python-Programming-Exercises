#!python

# bubbleSort() function with a list parameter named numbers. 
# The function rearranges the values in this list in-place. 
# The function also returns the now-sorted list. There are 
# many sorting algorithms, but this exercise asks you to 
# implement the bubble sort algorithm.

def bubbleSort(numbers):
    # The outer loop loops i over all but the last number:
    for i in range(len(numbers) - 1):
        # The inner loop loops j starting at i to the last number:
        for j in range(i, len(numbers)):
            # If the number at i is greater than the number at j, swap them:
            if numbers[i] > numbers[j]:
                numbers[i], numbers[j] = numbers[j], numbers[i]
    # Return the now-sorted list:
    return numbers

