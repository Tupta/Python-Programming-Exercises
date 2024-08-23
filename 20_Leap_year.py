#!python

#LeapYear() function with an integer year parameter. 
#If year is a leap year, the function returns True. 
#Otherwise, the function returns False.

def isLeapYear(year):
# Years divisible by 4 and 400 are leap years
# But, years divisible by 100 are not leap years

    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    # Every other year is not a leap year:
    else:
        return False
    
#Asseration
assert isLeapYear(1999) == False
assert isLeapYear(2000) == True
assert isLeapYear(2001) == False
assert isLeapYear(2004) == True
assert isLeapYear(2100) == False
assert isLeapYear(2400) == True

print('all test passed')