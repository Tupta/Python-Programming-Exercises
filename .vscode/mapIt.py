#!python3

# Program otwierający miejsce na google maps w przeglądarce którego adres jest skopiowany w pamięci podręcznej, lub uruchamiamy program z podaniem tego adresu:
#Jeżeli teraz uruchomisz program za pomocą polecenia w wierszu poleceń: mapit chorzów, brzozowa5 

import webbrowser, sys, pyperclip, requests

if len(sys.argv) >1 :
   # Pobranie adresu z wiersza poleceń.
    adress = ' '.join(sys.argv[1:])
else:
    # Pobranie adresu ze schowka.
    address = pyperclip.paste()
webbrowser.open('https://www.google.pl/maps/place/' + address)

# Jak dodasz jeszcze kilka poleceń z serii webbrowser.open jak poniżej to program bedezie otwieral kolejne strony :)
# webbrowser.open('https://www.interia.pl')
# webbrowser.open('https://www.pogoda.pl')
# webbrowser.open('https://www.zhp.pl')