#!python 

# Function with parameters year, month, and day. 
# # The function should return True if the integers 
# # provided for these parameters represent a valid date. 
# # Otherwise, the function returns False. 


#Import leap_year for 29th February of leap year 

from 20_Leap_year.py import isLeapYear 

# # Main function 

def isValidDate(year, month, day): 
    
    # # First, check if the month is within the valid range 
    if month < 1 or month > 12: 
        return False 

    # Check months with 31 days 
    if month in {1, 3, 5, 7, 8, 10, 12}: 
        if 1 <= day <= 31: 
            return True 
        else: 
            return False 
    # Check months with 30 days 

    elif month in {4, 6, 9, 11}: 
        if 1 <= day <= 30: 
            return True 
        else: return False 

    # Special case for February (month 2) 

    elif month == 2: 
        # If leap year, February can have 29 days 
        if isLeapYear(year): 
            if 1 <= day <= 29: 
                return True 
            else: 
                return False 
            
        # Non-leap year, February has 28 days 
        
        else: 
            if 1 <= day <= 28: 
                return True 
            else: 
                return False 

    # If none of the conditions are met, return False 
    return False 

#Assertions (test cases) 

assert isValidDate(1999, 12, 31) == True 
assert isValidDate(2000, 2, 29) == True 
assert isValidDate(2001, 2, 29) == False 
assert isValidDate(2029, 13, 1) == False 
assert isValidDate(1000000, 1, 1) == True 
assert isValidDate(2015, 4, 31) == False 
assert isValidDate(1970, 5, 99) == False 
assert isValidDate(1981, 0, 3) == False 
assert isValidDate(1666, 4, 0) == False 