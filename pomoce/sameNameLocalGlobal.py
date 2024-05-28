def spam():
    global eggs
    eggs = 'spam'  # To jest zmienna globalna.

def bacon():
    eggs = 'bacon'  # To jest zmienna lokalna.

def ham():
    print(eggs)  # To jest zmienna globalna.

 eggs = 42  # To jest zmienna globalna.
 spam()
 print(eggs)
