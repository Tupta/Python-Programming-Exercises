word=input("podaj słowo które chcesz zobaczyć zapisane wspak: ")
print("twoje słowo to: ", word)
new_word = word[::-1]

# W Pythonie, łańcuchy znaków są traktowane jako sekwencje, a składnia [::-1] odwraca każdą sekwencję, bez względu na to, ile elementów zawiera.
print("twoje słowo pisane wspak wygląda anstępująco: ",new_word)


# jest jeszcze inny sposób a mianowicie: new_word = ''.join(reversed(word))
#albo przez iteracje łańcucha jakim jest slowo/zmienna "word" tak jak w kodzie ponizej

# word = "Tupta"
# new_word = ""
# for znak in word:
#     new_word = znak + new_word
# print(new_word)
Oznacza to, że kod będzie musiał wykonywać przedstawione
poniżej zadania.