#!python

#Find And Replace

#Simply program/function for replacing text.
#findAndReplace() function has three parameters: text is the string
# with text to be replaced, oldText is the text to be replaced, 
# and newText is the replacement text. 

def findAndReplace(text, oldText, newText):
    result = text.replace(oldText, newText)
    print('result')
    