# Temperature Conversion

# Converting between Celsius and Fahrenheit involves a basic calculation and provides 
# a good exercise for writing functions that take in a numeric input and return a numeric output.

def convertToFahrenheit(x):
    Fahrenheit = x * (9/5) + 32
    print(f'{x} degrees Celsius converted to Fahrenheit equals {Fahrenheit}')
    return Fahrenheit

def convertToCelsius(x):
    Celsius = (x - 32) * (5/9)
    print(f'{x} degrees Fahrenheit converted to Celsius equals {Celsius}')
    return Celsius

# Assertions
assert convertToCelsius(0) == -17.77777777777778
assert convertToCelsius(180) == 82.22222222222223
assert convertToFahrenheit(0) == 32
assert convertToFahrenheit(100) == 212
assert convertToCelsius(convertToFahrenheit(15)) == 15

print('\n\n\n')

print(f'Hello. This simple program converts temperature from Celsius '
      'to Fahrenheit and vice versa.'
      '\n\n'
      )

yourChoice = ''
while yourChoice != 'q':
    x = input('Enter degrees value to convert:> ')
    if not x.replace('.', '').replace('-', '').isdigit():
        print("Please enter a valid number.")
        continue
    try:
        x = float(x)
    except ValueError:
        print("Please enter a valid number.")
        continue
    
    yourChoice = input('Which conversion would you like to perform? '
                       'Press 1 if you want to convert Celsius to Fahrenheit, '
                       'press 2 if you want to convert Fahrenheit to Celsius, '
                       'or press "q" if you want to quit: ')
    if yourChoice == '1':
        convertToFahrenheit(x)
    elif yourChoice == '2':
        convertToCelsius(x)
