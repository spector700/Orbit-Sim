from numpy.random import uniform
import pygame
from pygame.math import Vector2 as vec2

from sprites import Stars, Bodies


class CameraGroup(pygame.sprite.Group):

    """
    SPRITE GROUP SUBCLASS TO HANDLE MOUSE INPUTS AS OFFSETS FOR A 'CAMERA'
        - CLICK AND DRAG CAMERA
        - SCROLL WHEEL ZOOM
        - SPACE BAR TO RESET POSITIONS
    """

    def __init__(self):
        super().__init__()
        self.offset = pygame.math.Vector2()  # TO APPLY TO SPRITES
        self.clickstart_offset = pygame.math.Vector2()  # NORMALISE AFTER CLICK
        self.dragging = False
        self.incriment_up = 1.41
        self.incriment_down = 0.7
        self.reset_scales()

    def reset_scales(self):
        self.offset.x = 0
        self.offset.y = 0
        self.scale_size = 0.8
        # self.scale_velocity = 0.001
        # self.scale_distance = 0.001

    def scale(self, direction):
        self.offset.x *= direction
        self.offset.y *= direction
        self.scale_size *= direction
        # self.scale_velocity *= direction
        # self.scale_distance *= direction

    def mouse_camera(self, event):
        # If left mouse button was pressed
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            self.dragging = True
            mouse_x, mouse_y = pygame.mouse.get_pos()
            self.clickstart_offset.x = self.offset.x - mouse_x
            self.clickstart_offset.y = self.offset.y - mouse_y

        # Turn off dragging if left mouse button was released
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            self.dragging = False

        # If mouse moved when button was pressed
        elif event.type == pygame.MOUSEMOTION:
            if self.dragging:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                # Add the start offset with the mouse positions
                self.offset.x = mouse_x + self.clickstart_offset.x
                self.offset.y = mouse_y + self.clickstart_offset.y

        # If Mouse wheel UP
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 4:
            self.scale(self.incriment_up)

        # If Mouse wheel DOWN
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 5:
            self.scale(self.incriment_down)

        # If SPACE was pressed
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            self.reset_scales()

        # Spawn satellite with right mouse button
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            Bodies(
                self,
                pos=vec2(mouse_x - self.offset.x, mouse_y - self.offset.y),
                radius=9,
                mass=2000,
                vel=vec2(1370, 100),
            )

    def create_sprites(self, amount, width, height):
        # Create all the Stars
        for _ in range(amount):
            Stars(self)

        Bodies(
            self,
            pos=vec2(width, height),
            radius=100,
            color="#6b93d6",
            mass=5.97219e24,
            vel=vec2(-24.947719394204714 / 2, 0),
            protected=True,
        )
        Bodies(
            self,
            pos=vec2(width, height / 3),
            radius=20,
            color="gray",
            mass=7.349e22,
            vel=vec2(1023, 0),
            protected=True,
        )
