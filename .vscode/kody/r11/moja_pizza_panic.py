# Pizza Panic
# Gracz musi złapać lecące w dół pizze, zanim spadną na ziemię

from superwires import games, color
import random

games.init(screen_width=640, screen_height=480, fps=50)


class Pan(games.Sprite):
    """Patelnia do łapania pizzy"""
    image = games.load_image("patelnia.bmp")
    
    def __init__(self):
        super(Pan, self).__init__(image = Pan.image,
                                 x = games.mouse.x,
                                 bottom = games.screen.height)
        self.score = games.Text(value = 0, size = 30, color = color.black, top = 5, right = games.screen.width - 10)
        games.screen.add(self.score)
        
    def update(self):
        """Zmiana pozycji patelni przy użyciu myszy w osi x"""
        self.x = games.mouse.x
        
        if self.left < 0:
            self.left = 0
        if self.right > games.screen.width:
            self.right = games.screen.width
            
        self.check_catch()
    
    def check_catch(self):
        """SPrawdzenie czy złapano pizze"""
        for pizza in self.overlapping_sprites:
            self.score.value += 10
            self.score.right = games.screen.width -10
            pizza.handle_caught()

class Pizza(games.Sprite):
    """Pizza spadajaca na ziemie"""
    image =games.load_image("pizza.bmp")
    speed = 1
    
    def __init__(self, x, y = 90):
        """Inicjalizuj obiekt klasy pizza"""
        super(Pizza, self).__init__(image = Pizza.image, 
                                    x = x, y = y,
                                    dy = Pizza.speed)
    def update(self):
        """sprawdzenie czy pizza dotknela dolnego brzegu ekranu czyli ziemi"""
        if self.bottom > games.screen.height:
            self.end_game()
            self.destroy()
            
    def handle_caught(self):
        """Zniszcz pizze gdy zostaje złapana"""
        self.destroy()
        
    def end_game(self):
        """koniec gry"""
        end_message = games.Message(value = "Koniec gry",
                                    size = 90,
                                    color = color.red,
                                    x = games.screen.width/2,
                                    y = games.screen.height/2,
                                    lifetime = 5 *  games.screen.fps,
                                    after_death= games.screen.quit)
        games.screen.add(end_message)

class Chef(games.Sprite):
    """Szef kuchni zrzucający pizze i poruszajacy sie na calej szerokosci ekrqnu"""
    image = games.load_image("kucharz.bmp")
    
    def __init__(self, y = 55, speed = 2, odds_change = 200):
        """uruchomienie inicjalizacja objektu szefa kuchni"""
        super(Chef, self).__init__(image = Chef.image,
                                    x = games.screen.width / 2,
                                    y = y,
                                    dx = speed)
        self.odds_change = odds_change
        self.time_til_drop = 0
        
    def update(self):
        """Czy zmiana keirunku na przeciwny jest koneiczna"""
        if self.left < 0 or self.right > games.screen.width:
            self.dx = -self.dx
        elif random.randrange(self.odds_change) ==0:
            self.dx = -self.dx
        self.check_drop()
        
    def check_drop(self):
        """Zmniejsza licznik odliczajacy czas do zrzucenia pizzy lub zrczuca od razu i resetuje """
        if self.time_til_drop > 0:
            self.time_til_drop -= 1
        else:
            new_pizza = Pizza(x = self.x)
            games.screen.add(new_pizza)
            # ustawia margines na 30% wysokości pizzy, niezależnie od predkosci pizzy
            self.time_til_drop = int(new_pizza.height * 1.3 / Pizza.speed) + 1
            
def main():
    """uruchom gre"""
    wall_image = games.load_image("sciana.jpg", transparent = False)
    games.screen.background = wall_image
    
    the_chef = Chef()
    games.screen.add(the_chef)
    
    the_pan = Pan()
    games.screen.add(the_pan)
    
    games.mouse.is_visible = False
    games.screen.event_grab = True
    games.screen.mainloop()
    
#wystartuj

main()
        

