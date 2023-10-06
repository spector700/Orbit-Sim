from sys import exit

import pygame
from pygame.locals import KEYDOWN, K_ESCAPE, K_f

from camera import CameraGroup

WIDTH = 800
HEIGHT = 800
STARS = 1000


pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([WIDTH, HEIGHT])
clock = pygame.time.Clock()
font = pygame.font.SysFont("monospace", 25)

# Inistiallize Camera
visible = CameraGroup()

# Create all the sprites with the amount of stars
visible.create_sprites(STARS)


def run():
    fps = False
    # Run until the user asks to quit
    while True:
        clock.tick(120)

        pygame.transform.rotozoom(screen, 120.5, 0.5)
        visible.update()
        pygame.display.update()

        screen.fill("black")

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

            visible.mouse_camera(event)

        # Show FPS if 'f' was pressed
        if fps:
            text = font.render("FPS: " + str(round(clock.get_fps())), True, "white")
            screen.blit(text, (0, 0))


if __name__ == "__main__":
    run()
