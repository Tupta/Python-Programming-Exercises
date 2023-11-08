# def boxPrint(symbol, width, height):
#     if len(symbol) != 1:
#         raise Exception('Symbol musi być pojedynczym znakiem.')
#     if width <= 2:
#         raise Exception('Szerokość musi mieć wartość większą niż2.')
#     if height <= 2:
#         raise Exception('Wysokość musi mieć wartość większą niż    2.')
#     print(symbol * width)
#     for i in range(height - 2):
#         print(symbol + (' ' * (width - 2)) + symbol)
#         print(symbol * width)
#     for sym, w, h in (('*', 4, 4), ('O', 20, 5), ('x', 1, 3), ('ZZ',3, 3)):
#         try:
#             boxPrint(sym, w, h)
#         except Exception as err:
#             print('Nastąpiło zgłoszenie wyjątku: ' + str(err))

import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.debug('Początek programu')

def factorial(n):
    logging.debug('Początek wywołania funkcji factorial(%s%%)' %(n))
    total = 1
    for i in range(1, n + 1):
        total *= i
        logging.debug('i wynosi ' + str(i) + ', wartość całkowitawynosi ' + str(total))
        logging.debug('Koniec wywołania funkcji factorial(%s%%)' %(n))
    return total
print(factorial(5))
logging.debug('Koniec programu')