#!python

#Stop gninnipS My sdroW!
# Write a function that takes in a string of one or more words, and returns the same string, 
# but with all five or more letter words reversed (Just like the name of this Kata). 
# Strings passed in will consist of only letters and spaces. 
# Spaces will be included only when more than one word is present.

def spin_words(sentence):
    sentence =sentence.split(' ')

    reversed_words = [word[::-1] if len(word) >= 5 else word for word in sentence]

    reversed_sentence = ' '.join(reversed_words)
    print(reversed_sentence)

sentence = 'Welcome'

print(spin_words(sentence))