# program obliczający ilość orzełkow i reszek w okreslonej liczbie rzutow moneta


import random
lrzutow=1
orzel=0
reszka=0


while lrzutow <=100:
        x = random.randint(0, 1) 
        #print(x)
        if x == 0:
            orzel += 1
        else:
            reszka += 1
        lrzutow += 1
    


print("liczba wyrzuconych orłow: ", orzel, "a liczba wyrzuconych reszek: ", reszka)

input("\n\nAby zakończyć program, naciśnij klawisz Enter.") 
