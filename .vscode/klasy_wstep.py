class Człowiek(object):
    def __init__(self, imie, wiek):
        self.imie = imie
        self.wiek = wiek
        
    imie = "sztefan"
    kolor = "niebieskiego"
    
    
    def przedstawsie(self, powitanie = "Cześć Ci "):
        #return "cześć mam na imie" + self.imie 
        print("cześć mam na imie ", self.imie, "mam "+ str(self.wiek) + " lat")
    
    def wzrost(self):
        print("mam 180cm wzrostu, ale ze mnie wielki", self.imie)
        
    def koloroczu(self):
        print ("mam oczy koloru", self.kolor )


#main
obiekt = Człowiek("stefcio",20)
print(obiekt.imie)
obiekt.przedstawsie()
obiekt.wzrost()
obiekt.koloroczu()

obiekt2 = Człowiek("adiiiii", 99)
obiekt2.imie = " Adi"
print(obiekt2.przedstawsie())
print(obiekt.imie)
obiekt.przedstawsie()
obiekt2.przedstawsie()

