from sys import exit

import pygame
from pygame.locals import KEYDOWN, K_ESCAPE, K_f

WIDTH = 800
HEIGHT = 800
STARS = 2000


pygame.init()

from camera import CameraGroup

# Set up the drawing window
screen = pygame.display.set_mode([WIDTH, HEIGHT])
trace = pygame.Surface((WIDTH, HEIGHT))
clock = pygame.time.Clock()
font = pygame.font.SysFont("monospace", 25)

# Inistiallize Camera
group = CameraGroup()

# Create all the sprites with the amount of Stars
group.create_sprites(STARS, WIDTH / 2, HEIGHT / 2)


def run():
    fps = False
    # Run until the user asks to quit
    while True:
        clock.tick(60)

        screen.fill("black")
        group.update()

        # Event loop
        for event in pygame.event.get():
            # Did the user click the window close button?
            if event.type == pygame.QUIT or (
                event.type == KEYDOWN and event.key == K_ESCAPE
            ):
                pygame.quit()
                exit()

            if event.type == KEYDOWN and event.key == K_f and fps:
                fps = False
            elif event.type == KEYDOWN and event.key == K_f and not fps:
                fps = True

            group.mouse_camera(event)

        # Show FPS if 'f' was pressed
        if fps:
            text = font.render("FPS: " + str(round(clock.get_fps())), True, "white")
            screen.blit(text, (0, 0))

        pygame.display.update()


if __name__ == "__main__":
    run()
