def a():
    print('Rozpoczęcie wykonywania funkcji a()')
    spam = 42
    b()
    d()
    print('Zakończenie wykonywania funkcji a()')

def b():
    print('Rozpoczęcie wykonywania funkcji b()')
    spam = 101
    c()
    print('Zakończenie wykonywania funkcji b()')

def c():
    print('Rozpoczęcie wykonywania funkcji c()')
    print('Zakończenie wykonywania funkcji c()')

def d():
    print('Rozpoczęcie wykonywania funkcji d()')
    print('Zakończenie wykonywania funkcji d()')

a()
