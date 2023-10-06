import pygame
from numpy.random import choice, uniform


class Stars(pygame.sprite.Sprite):
    def __init__(self, sprite_group):
        super().__init__(sprite_group)
        self.sprite_group = sprite_group
        star_colors = [
            "lightblue",
            "white",
            "lightyellow",
            "lightgray",
            "gray",
            "darkgray",
        ]

        self.color = choice(star_colors)

        self.surface = pygame.display.get_surface()
        x, y = pygame.display.get_surface().get_size()

        self.x = round(uniform(-300, x + 300))
        self.y = round(uniform(-300, y + 300))

        self.base_size = uniform(1, 1.2)

    def update(self):
        self.draw()

    def draw(self):
        pos = (
            self.x + self.sprite_group.offset.x * 0.1 * self.base_size,
            self.y + self.sprite_group.offset.y * 0.1 * self.base_size,
        )
        pygame.draw.circle(self.surface, self.color, pos, self.base_size)


class Earth(Stars):
    def __init__(self, sprite_group):
        super().__init__(sprite_group)
        x, y = pygame.display.get_surface().get_size()
        self.x = x / 2
        self.y = y / 2
        self.base_size = 100
        self.color = "#6b93d6"

    def draw(self):
        self.zoom = self.base_size * self.sprite_group.scale_size
        pos = (
            self.x + self.sprite_group.offset.x * 0.5,
            self.y + self.sprite_group.offset.y * 0.5,
        )
        pygame.draw.circle(self.surface, self.color, pos, self.zoom)
