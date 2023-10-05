import pygame
from numpy.random import uniform, randint, choice

class Stars(pygame.sprite.Sprite):
    def __init__(self, sprite_group):
        super().__init__(sprite_group)
        self.sprite_group = sprite_group
        star_colors = ['lightblue', 'white', 'lightyellow', 'lightgray', 'orange', 'red']

        self.color = choice(star_colors)
        self.surface = pygame.display.get_surface()
        x, y = pygame.display.get_surface().get_size()

        self.x = round(uniform(-300,x + 300)) 
        self.y = round(uniform(-300,y + 300))

        self.size = randint(0.5, 2.0)

    def update(self):
        self.draw()

    def draw(self):
        pos = (self.x + self.sprite_group.offset.x*0.3, self.y + self.sprite_group.offset.y*0.3)
        pygame.draw.circle(
            self.surface,
            self.color,
            pos,
            self.size)


class Earth(Stars):
    def __init__(self, sprite_group):
        super().__init__(sprite_group)
        x, y = pygame.display.get_surface().get_size()
        self.x = x / 2
        self.y = y / 2
        self.size = 100
        self.color = "#6b93d6"
