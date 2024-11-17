#!python

#commaFormat() function with a number parameter. 
# The argument for this parameter can be an integer 
# or floating-point number. Your function returns a 
# string of this number with proper US/UK comma formatting. 
# There is a comma # after every third digit in the whole 
# number part.

def commaFormat(number):

    # Convert number to string for manipulation
    num_str = str(number)

    # Sprawdź, czy liczba ma część ułamkową
    if '.' in num_str:
        fractionalPart = num_str[num_str.index('.'):]  # Wyciągamy część dziesiętną
        wholePart = num_str[:num_str.index('.')]  # Wyciągamy część całkowitą
    else:
        fractionalPart = ''
        wholePart = num_str

    # Zmienna do przechowywania przekształconego ciągu znaków
    commaNumber = ''
    triplet = ''

    # Loop over the digits starting from the right to left for the whole number part
    for i in range(len(wholePart) - 1, -1, -1):
        # Dodaj cyfry do zmiennej triplet
        triplet = wholePart[i] + triplet
        # Gdy triplet ma trzy cyfry, dodaj go z przecinkiem do wynikowego ciągu znaków
        if len(triplet) == 3:
            commaNumber = triplet + ',' + commaNumber
            triplet = ''  # Resetuj triplet po dodaniu do wyniku

    # Jeśli zostały jakieś cyfry (mniej niż trzy) w triplet, dodaj je
    if triplet != '':
        commaNumber = triplet + ',' + commaNumber

    # Zwróć wynik, usuwając ostatni przecinek, jeśli istnieje
    return commaNumber.rstrip(',') + fractionalPart


# Testowanie
assert commaFormat(1) == '1'
assert commaFormat(10) == '10'
assert commaFormat(100) == '100'
assert commaFormat(1000) == '1,000'
assert commaFormat(10000) == '10,000'
assert commaFormat(100000) == '100,000'
assert commaFormat(1000000) == '1,000,000'
assert commaFormat(1234567890) == '1,234,567,890'
assert commaFormat(1000.123456) == '1,000.123456'
print('all tests passed, serio serio :)')
