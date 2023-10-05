from sprites import Stars,Earth
from numpy.random import uniform
import pygame

class CameraGroup(pygame.sprite.Group):
    """
    SPRITE GROUP SUBCLASS TO HANDLE MOUSE INPUTS AS OFFSETS FOR A 'CAMERA'
        - CLICK AND DRAG CAMERA
        - SCROLL WHEEL ZOOM
        - SPACE BAR TO RESET POSITIONS
    """
    def __init__(self):
        super().__init__()
        self.offset = pygame.math.Vector2() #TO APPLY TO SPRITES
        self.clickstart_offset = pygame.math.Vector2() #NORMALISE AFTER CLICK
        self.dragging = False #WHEN TO APPLY OFFSET TO SPRITES
        self.reset_scales()

    def reset_scales(self):
        self.offset.x = 0
        self.offset.y = 0
        self.scale_size = 0

    def scale(self, direction):
        self.offset.x *= direction
        self.offset.y *= direction
        self.scale_size *= direction
        self.scale_velocity *= direction
        self.scale_distance *= direction

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

    def create_sprites(self):
        # Create all the Stars
        for i in range(2000):
            Stars(self)
        # Create the Earth
        Earth(self)


