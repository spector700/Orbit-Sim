import pygame


class Explosion(pygame.sprite.Sprite):
    def __init__(self, filename):
        super().__init__()
        self.spritesheet = pygame.image.load(filename).convert_alpha()
        self.surface = pygame.display.get_surface()
        self.play = False

        self.animation_rows = 6
        self.animation_columns = 8
        self.frames = []
        width = 256
        height = 256
        frame = 0

        for i in range(self.animation_rows):
            for _ in range(self.animation_columns):
                self.frames.append(self.get_image(frame, width, height, 0.5, i))
                frame += 1

        self.index = 0
        self.image = self.frames[self.index]
        self.rect = self.image.get_rect()

    def get_image(self, frame, width, height, scale, row):
        """get each image from the sprite sheet"""

        x = frame % self.animation_columns * width
        y = row * height
        # Make each image transparent
        image = pygame.Surface((width, height), pygame.SRCALPHA)
        image.blit(self.spritesheet, (0, 0), (x, y, width, height))
        image = pygame.transform.scale(image, (width * scale, height * scale))

        return image

    def animate(self, pos):
        self.play = True
        self.pos = pos

        boom = pygame.mixer.Sound("assets/boom.wav")
        boom.set_volume(0.3)
        boom.fadeout(2)
        boom.play(fade_ms=50)

    def update(self, speed, camera_group):
        if self.play:
            self.index += speed

            if int(self.index) >= len(self.frames):
                self.index = 0
                self.play = False
                self.kill()

            self.rect.center = self.pos + camera_group.offset
            self.image = self.frames[int(self.index)]
