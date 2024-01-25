def spam():
    print(eggs)  # BŁĄD!
    eggs = 'Zmienna lokalna funkcji spam().'

eggs = 'zmienna globalna'
spam()
