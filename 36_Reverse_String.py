#!python

#reverseString() function with a text parameter. 
# The function should return a string with 
# all of text’s characters in reverse order.

def reverseString(text):
    # Convert the text string into a list of character strings:
    text = list(text)
    # Loop over the first half of indexes in the list:
    for i in range(len(text) // 2):
        # Swap the values of i and it's mirror index in the second
        # half of the list:
        mirrorIndex = len(text) - 1 - i
        text[i], text[mirrorIndex] = text[mirrorIndex], text[i]
        # Join the list of strings into a single string and return it:
    return ''.join(text)

#Asseration
assert reverseString('Hello') == 'olleH'
assert reverseString('') == ''
assert reverseString('aaazzz') == 'zzzaaa'
assert reverseString('xxxx') == 'xxxx'
print ('all tests passed')