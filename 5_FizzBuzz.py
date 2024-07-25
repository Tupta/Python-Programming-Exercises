#!python

# FizzBuzz Fizz is a simply word game, where fizzBuzz function 
# prints one of four things:

#1.Prints 'FizzBuzz' if the number is divisible by 3 and 5.

#2.Prints 'Fizz' if the number is only divisible by 3.

#3.Prints 'Buzz' if the number is only divisible by 5.

#4.Prints the number if the number is neither divisible by 3 nor 5. 

def fizzBuzz(upTo):
    # Loop from 1 up to (and including) the upTo parameter:
    for number in range(1, upTo + 1):
        # If the loop number is divisible by 3 and 5, print 'FizzBuzz':
        if number % 3 == 0 and number % 5 == 0:
            print('FizzBuzz', end=' ')
        # Otherwise the loop number is divisible by only 3, print 'Fizz':
        elif number % 3 == 0:
            print('Fizz', end=' ')
        # Otherwise the loop number is divisible by only 5, print 'Buzz':
        elif number % 5 == 0:
            print('Buzz', end=' ')
        # Otherwise, print the loop number:
        else:
            print(number, end=' ')


#And now simply modify to make some assertions. 
# Be cause first version of function didn't return anything
# I attached list "result" where function will return some results wchih
#can be used for asserations. 
def fizzBuzz(upTo):
    result = []
    # Loop from 1 up to (and including) the upTo parameter:
    for number in range(1, upTo + 1):
        # If the loop number is divisible by 3 and 5, append 'FizzBuzz' to result:
        if number % 3 == 0 and number % 5 == 0:
            result.append('FizzBuzz')
        # Otherwise if the loop number is divisible by only 3, append 'Fizz' to result:
        elif number % 3 == 0:
            result.append('Fizz')
        # Otherwise if the loop number is divisible by only 5, append 'Buzz' to result:
        elif number % 5 == 0:
            result.append('Buzz')
        # Otherwise, append the loop number to result:
        else:
            result.append(str(number))
    return ' '.join(result)

# Assertion

assert fizzBuzz(1) == '1'
assert fizzBuzz(25) == '1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz 16 17 Fizz 19 Buzz Fizz 22 23 Fizz Buzz'

print('All tests passed')
