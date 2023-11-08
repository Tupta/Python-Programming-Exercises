## Gra wisielec

import sys

number_of_tries = 5
word = "kamila"
used_letters = []
user_word = []

def find_indexes(word, letter):
    indexes = []
    
    for index, letter_in_world in enumerate(word):
        if letter == letter_in_world:
            indexes.append(index)
              
    
    return indexes
    
def show_game_status():
    print()
    print(user_word)
    print()
    print("Pozostało jeszcze ", number_of_tries,"prób")
    print()
    print("Użyłeś już takie litery jak:", used_letters)
    print()
    

for _ in word:
    user_word.append("_")

while True:
    letter =input("podaj literę: ")
    print()
    used_letters.append(letter)
    
    found_indexes = (find_indexes(word, letter))
    
    if len(found_indexes) == 0:
        print("Nie ma takiej litery")
        number_of_tries -= 1
        
        
        if number_of_tries == 0:
            print("koniec gry GAME OVER KUP SE ROWER")
            sys.exit(0)
    
    else:
        for index in found_indexes:
            user_word[index] = letter
        
                
        #Poniżej sposób żeby wyświetlić słowo jako jedno słowo a nie listę liter ['f','g' itd.] dlatego generujemy pustego stringa ""idołączam do niego litery spelniajace wymaganie
        print("".join(user_word))
        if "".join(user_word) == word:
            print("Brawo odgadłeś słowo")
            sys.exit(0)
            
    show_game_status()


    
