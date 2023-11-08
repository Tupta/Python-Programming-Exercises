# Gra w kamień papier nożyce

import random

# intro
print("Witaj! Masz ochotę zagrać w grę Kamień, Papier, Nożyce?")

# player choice
playerchoice = input("Podaj swój typ, wybierając:\n1. Kamień, 2. Papier lub 3. Nożyce: ")

if playerchoice == '1':
    player_choice_text = "Kamień"
elif playerchoice == '2':
    player_choice_text = "Papier"
elif playerchoice == '3':
    player_choice_text = "Nożyce"
else:
    print("Nieprawidłowy wybór. Spróbuj jeszcze raz.")
    exit()

print("Wybrałeś:", player_choice_text)

# computer choice
choices = ["Kamień", "Papier", "Nożyce"]
computerchoice = random.choice(choices)
print("Komputer wybrał:", computerchoice)

# Sprawdzenie wyników
if player_choice_text == computerchoice:
    print("Remis")
elif (player_choice_text == "Kamień" and computerchoice == "Nożyce") or (player_choice_text == "Papier" and computerchoice == "Kamień") or (player_choice_text == "Nożyce" and computerchoice == "Papier"):
    print('Brawo, wygrałeś!')
else:
    print('Niestety przegrałeś.')