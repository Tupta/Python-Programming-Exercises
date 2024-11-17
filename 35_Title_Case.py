#!python

#getTitleCase() function with a text parameter. The function should return the title 
# case form of the string: every word begins with an uppercase and the remaining letters are lowercase. 
# Non-letter characters separate words in the string

def getTitleCase(text):
    # Create a titledText variable to store the titlecase text:
    titledText = ''
    # Loop over every index in text:
    for i in range(len(text)):
        # The character at the start of text should be uppercase:
        if i == 0:
            titledText += text[i].upper()
        # If the character is a letter and the previous character is
        # not a letter, make it uppercase:
        elif text[i].isalpha() and not text[i - 1].isalpha():
            titledText += text[i].upper()
        # Otherwise, make it lowercase:
        else:
            titledText += text[i].lower()
    # Return the titled cased string:
    return titledText


#Asserations

assert getTitleCase('Hello, world!') == 'Hello, World!'
assert getTitleCase('HELLO') == 'Hello'
assert getTitleCase('hello') == 'Hello'
assert getTitleCase('hElLo') == 'Hello'
assert getTitleCase('') == ''
assert getTitleCase('abc123xyz') == 'Abc123Xyz'
assert getTitleCase('cat dog RAT') == 'Cat Dog Rat'
assert getTitleCase('cat,dog,RAT') == 'Cat,Dog,Rat'
print ("all tests passed")