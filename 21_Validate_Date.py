#!python

# here write info about the program

#import leap_year for 29 feb of leap year
from 20_Leap_year import isLeapYear(year)


#main def
def isValidDate(day, month, year):
    #long if but i'am a little but lazy today :) 
    if 0 < day <= 31 and 1 <= month <=12 and year >=1:
        return True
    else:
        return False
    
    
#asserations

assert isValidDate(1999, 12, 31) == True
assert isValidDate(2000, 2, 29) == True
assert isValidDate(2001, 2, 29) == False
assert isValidDate(2029, 13, 1) == False
assert isValidDate(1000000, 1, 1) == True
assert isValidDate(2015, 4, 31) == False
assert isValidDate(1970, 5, 99) == False
assert isValidDate(1981, 0, 3) == False
assert isValidDate(1666, 4, 0) == False