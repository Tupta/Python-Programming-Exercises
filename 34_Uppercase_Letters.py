#!python


# Uppercase Letters etUppercase() function with a text string parameter. The function returns 
# a string with all lowercase letters in text converted to uppercase. Any non-letter characters 
# in text remain as they are. For example, 'Hello' causes getUppercase() to return 'HELLO' but 
# 'goodbye 123!' returns 'GOODBYE 123!'.


def getUppercase(text):
    # Map the lowercase letters to uppercase letters.
    LOWER_TO_UPPER = {
        'a': 'A', 'b': 'B', 'c': 'C', 'd': 'D', 'e': 'E', 'f': 'F', 'g': 'G',
        'h': 'H', 'i': 'I', 'j': 'J', 'k': 'K', 'l': 'L', 'm': 'M', 'n': 'N',
        'o': 'O', 'p': 'P', 'q': 'Q', 'r': 'R', 's': 'S', 't': 'T', 'u': 'U',
        'v': 'V', 'w': 'W', 'x': 'X', 'y': 'Y', 'z': 'Z'
    }

    # Create a new variable that starts as a blank string and will
    # hold the uppercase form of text:
    uppercaseText = ''

    # Loop over all the characters in text, adding non-lowercase
    # characters to our new string:
    for character in text:
        if character in LOWER_TO_UPPER:
            # Append the uppercase form to the new string:
            uppercaseText += LOWER_TO_UPPER[character]
        else:
            # Append the character as is:
            uppercaseText += character

    # Return the uppercase string:
    return uppercaseText

# Assertions
assert getUppercase('Hello') == 'HELLO'
assert getUppercase('hello') == 'HELLO'
assert getUppercase('HELLO') == 'HELLO'
assert getUppercase('Hello, world!') == 'HELLO, WORLD!'
assert getUppercase('goodbye 123!') == 'GOODBYE 123!'
assert getUppercase('12345') == '12345'
assert getUppercase('') == ''

print('All tests passed')
