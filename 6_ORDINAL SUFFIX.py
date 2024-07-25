#!python

#ORDINAL SUFFIX
#In English, ordinal numerals have suffixes such as the “th” in “30th”
# or “nd” in “2nd”. This function ordinalSuffix()  
# with an integer parameter named number and returns 
# a string of the number with its ordinal suffix. 
# For example, ordinalSuffix(42) should return the string '42nd'.

def ordinalSuffix(number):
    # 11, 12, and 13 have the suffix th:
    if number % 100 in (11, 12, 13):
        return str(number) + 'th'
    # Numbers that end with 1 have the suffix st:
    if number % 10 == 1:
        return str(number) + 'st'
    # Numbers that end with 2 have the suffix nd:
    if number % 10 == 2:
        return str(number) + 'nd'
    # Numbers that end with 3 have the suffix rd:
    if number % 10 == 3:
        return str(number) + 'rd'
    # All other numbers end with th:
    return str(number) + 'th'



#Asserations
assert ordinalSuffix(0) == '0th'
assert ordinalSuffix(1) == '1st'
assert ordinalSuffix(2) == '2nd'
assert ordinalSuffix(3) == '3rd'
assert ordinalSuffix(4) == '4th'
assert ordinalSuffix(10) == '10th'
assert ordinalSuffix(11) == '11th'
assert ordinalSuffix(12) == '12th'
assert ordinalSuffix(13) == '13th'
assert ordinalSuffix(14) == '14th'
assert ordinalSuffix(101) == '101st'

print('All tests passed')