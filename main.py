import pygame
from sys import exit
from pygame.locals import *
from camera import CameraGroup
from sprites import Stars


WIDTH = 800
HEIGHT = 800

up = K_UP
down = K_DOWN
left = K_LEFT
right = K_RIGHT


pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([WIDTH, HEIGHT])
clock = pygame.time.Clock()

visible = CameraGroup()
visible.create_sprites()

def run():
    # Run until the user asks to quit
    while True:

        clock.tick(120)

        visible.update()
        pygame.display.update()

        # Event loop
        for event in pygame.event.get():
            # Did the user click the window close button?
            if event.type == pygame.QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                exit()

            visible.mouse_camera(event)

        screen.fill('black')

if __name__ == "__main__":
    run()

