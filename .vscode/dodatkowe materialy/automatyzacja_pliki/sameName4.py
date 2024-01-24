def spam():
    print(eggs)  # BŁĄD!
    eggs = 'Zmienna lokalna funkcji spam()'

eggs = 'Zmienna globalna'
spam()
