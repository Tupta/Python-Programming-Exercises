def spam():
    global eggs
    eggs = 'spam'

eggs = 'Zmienna globalna'
spam()
print(eggs)
