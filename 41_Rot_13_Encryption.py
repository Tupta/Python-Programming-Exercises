#!python


#rot13() function with a text parameter that returns 
# the ROT 13 encrypted version of text. Uppercase letters 
# encrypt to uppercase letters and lowercase letters encrypt 
# to lowercase letters. For example, 'HELLO, world!' encrypts 
# to 'URYYB, jbeyq!' and 'hello, WORLD!' encrypts to 'uryyb, JBEYQ!'.

def rot13(text):
    # Create an encryptedText variable to store the encrypted string:
    encryptedText = ''
    # Loop over each character in the text:
    for character in text:
        # If the character is not a letter, add it as-is to encryptedText:
        if not character.isalpha():
            encryptedText += character
        else:
            # Otherwise calculate the letter's "rotated 13" letter:
            rotatedLetterOrdinal = ord(character) + 13
            # If adding 13 pushes the letter past Z, subtract 26:
            if character.islower() and rotatedLetterOrdinal > 122:
                rotatedLetterOrdinal -= 26
            if character.isupper() and rotatedLetterOrdinal > 90:
                rotatedLetterOrdinal -= 26
            # Add the encrypted letter to encryptedText:
            encryptedText += chr(rotatedLetterOrdinal)
    # Return the encrypted text:
    return encryptedText


# Assertions:
assert rot13('Hello, world!') == 'Uryyb, jbeyq!'
assert rot13('Uryyb, jbeyq!') == 'Hello, world!'
assert rot13(rot13('Hello, world!')) == 'Hello, world!'
assert rot13('abcdefghijklmnopqrstuvwxyz') == 'nopqrstuvwxyzabcdefghijklm'
assert rot13('ABCDEFGHIJKLMNOPQRSTUVWXYZ') == 'NOPQRSTUVWXYZABCDEFGHIJKLM'
print('all tests passed')