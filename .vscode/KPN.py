#! python3


#Gra w kamień papier nożyce

import random

#intro :D
print("""witaj masz ochotę zagrać w grę Kamień, Papier, Nożyce ? """)

#player choice
playerchoice = int(input("Podaj swój typ wybierając:\n1. Kamień, 2.Papier lub 3. Nożyce "))

if playerchoice == 1:
    print('Wybrałeś Kamień')
    playerchoicetext = "Kamień"
elif playerchoice == 2 :
    print('Wybrałeś papier')
    playerchoicetext = "Papier"
elif playerchoice == 3 :
    playerchoicetext = "Nożyce"
    print('Wybrałeś Nożyce')
else :
    print('Żle wybrałeś jeszcze raz')

#computer choice
List = ["Kamień", "Papier", "Nożyce"]

computerchoice = random.choice(List)
print("Komputer wybrał " + computerchoice)

# Score check
if playerchoice == 1 and computerchoice == "Nożyce":
    print('Brawo, wygrałeś!')
elif playerchoice == 2 and computerchoice == "Kamień":
    print('Brawo, wygrałeś!')
elif playerchoice == 3 and computerchoice == "Papier":
    print('Brawo, wygrałeś!')
elif playerchoicetext == computerchoice:
    print("Remis")
else:
    print('Niestety przegrałeś.')