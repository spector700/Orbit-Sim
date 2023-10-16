from sys import exit

import pygame
from pygame.locals import K_ESCAPE, KEYDOWN, MOUSEBUTTONDOWN, K_f
from pygame.math import Vector2 as vec2

from camera import CameraGroup
from sprites import Bodies, Stars

WIDTH = 1920
HEIGHT = 1080
STARS = 2000


pygame.init()


# Set up the drawing window
screen = pygame.display.set_mode([WIDTH, HEIGHT])
trace = pygame.Surface((WIDTH, HEIGHT))
clock = pygame.time.Clock()
font = pygame.font.SysFont("monospace", 25)

# Camera group
camera_group = CameraGroup()
# Stars Group
backgroud = pygame.sprite.Group()
# Create all the stars
for _ in range(STARS):
    Stars(backgroud)

bodies_group = pygame.sprite.Group()

Bodies(
    bodies_group,
    pos=vec2(WIDTH / 2, HEIGHT / 2),
    radius=100,
    color="#6b93d6",
    mass=5.97219e24,
    vel=vec2(-24.947719394204714 / 2, 0),
    protected=True,
)
Bodies(
    bodies_group,
    pos=vec2(WIDTH / 2, HEIGHT / 2 + 270),
    radius=30,
    color="gray",
    mass=7.349e22,
    vel=vec2(1023, 0),
    protected=True,
)

animation_group = pygame.sprite.Group()

music = pygame.mixer.Sound("assets/interstellar-music.mp3")

music.set_volume(0.3)
music.play(-1, fade_ms=2000)


def run():
    fps = False
    # Run until the user asks to quit
    while True:
        clock.tick(60)
        screen.fill("black")

        backgroud.update(camera_group)
        bodies_group.update(camera_group, animation_group)

        animation_group.draw(screen)
        animation_group.update(0.3, camera_group)

        # Event loop
        for event in pygame.event.get():
            # Did the user click the window close button?
            if event.type == pygame.QUIT or (
                event.type == KEYDOWN and event.key == K_ESCAPE
            ):
                pygame.quit()
                exit()

            # Spawn satellite with right mouse button
            if event.type == MOUSEBUTTONDOWN and event.button == 3:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                Bodies(
                    bodies_group,
                    pos=vec2(
                        mouse_x - camera_group.offset.x, mouse_y - camera_group.offset.y
                    ),
                    radius=9,
                    mass=1500,
                    vel=vec2(1450, 50),
                )

            if event.type == KEYDOWN and event.key == K_f and fps:
                fps = False
            elif event.type == KEYDOWN and event.key == K_f and not fps:
                fps = True

            camera_group.mouse_camera(event)

        # Show FPS if 'f' was pressed
        if fps:
            text = font.render("FPS: " + str(round(clock.get_fps())), True, "white")
            screen.blit(text, (0, 0))

        camera_group.update()
        pygame.display.update()


if __name__ == "__main__":
    run()
