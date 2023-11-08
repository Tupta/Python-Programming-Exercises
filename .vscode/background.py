

from superwires import games, color
import random

games.init(screen_width = 640, screen_height = 480, fps = 50)

background_image = games.load_image("sciana.jpg", transparent = False)
games.screen.background = background_image


class Pan(games.Sprite):
    """Patelnia sterowana myszą"""
    def update(self):
        """współrzędne myszy"""
        self.x = games.mouse.x
        self.y = games.mouse.y
        self.check_collide()
        
    def check_collide(self):
        """spr4awdzenie czy nie dochodzi do kolizji z pizza"""
        for pizza in self.overlapping_sprites:
            pizza.handle_collide()

# class Pizza(games.Sprite):
#     """Sprężysta pizza."""
#     def update(self):
#         """Po dojechaniu do krawędzi składowa prędkości zmieni się na przeciwną"""
#         if self.right > games.screen.width or self.left < 0:
#             self.dx = -self.dx
#         if self.bottom > games.screen.height or self.top < 0:
#             self.dy = -self.dy

class Pizza(games.Sprite):
    """Nieuchwytna pizza."""
    def handle_collide(self):
        """przy kolizji przemieszczenie w losowe meijsce ekranu"""
        self.x = random.randrange(games.screen.width)
        self.y = random.randrange(games.screen.height)
    def update(self):
        """Po dojechaniu do krawędzi składowa prędkości zmieni się na przeciwną"""
        if self.right > games.screen.width or self.left < 0:
            self.dx = -self.dx
        if self.bottom > games.screen.height or self.top < 0:
            self.dy = -self.dy


pan_image = games.load_image("patelnia.bmp")
the_pan = Pan(image = pan_image,
                  x = games.mouse.x,
                  y = games.mouse.y,)
games.screen.add(the_pan)
games.mouse.is_visible = False
games.screen.event_grab = True

pizza_image = games.load_image("pizza.bmp")
pizza_x = random.randrange(games.screen.width)
pizza_y = random.randrange(games.screen.height)
the_pizza = Pizza(image = pizza_image,
                  x = pizza_x,
                  y = pizza_y,
                  dx = 1,
                  dy = 1,)


games.screen.add(the_pizza)

score = games.Text(value=199000,
                   size = 60,
                   color= color.red,
                   x= 550,
                   y = 30,)

games.screen.add(score)

games.screen.mainloop()