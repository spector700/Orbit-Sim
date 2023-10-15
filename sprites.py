import math

import pygame
from numpy.random import choice, uniform
from pygame.math import Vector2 as vec2

from spritesheet import Explosion


class Stars(pygame.sprite.Sprite):
    def __init__(self, sprite_group):
        super().__init__(sprite_group)
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

        self.size = uniform(1, 1.2)

    def update(self, camera_group):
        self.draw(camera_group)

    def draw(self, camera_group):
        pos = (
            self.x + camera_group.offset.x * 0.1 * self.size,
            self.y + camera_group.offset.y * 0.1 * self.size,
        )
        pygame.draw.circle(self.surface, self.color, pos, self.size)


class Bodies(pygame.sprite.Sprite):
    # 1 m = 1/1409466.667 pixlar
    SCALE = 1 / 1409466.667
    # Gravitational constant
    G = 6.67428e-11
    # The speed of time
    DT = 1 / 300

    _instances = []

    def __init__(
        self,
        sprite_group,
        pos=vec2(0, 0),
        color="white",
        radius=0,
        mass=0.0,
        vel=vec2(0, 0),
        protected=False,
    ):
        super().__init__(sprite_group)
        self.orbit = []
        self.width, self.height = pygame.display.get_surface().get_size()
        self.surface = pygame.display.get_surface()

        self.pos = pos
        self.color = color
        self.radius = radius
        self.mass = mass
        self.vel = vel
        self.protected = protected

        self.force_x = 0
        self.force_y = 0

        # Adds all the instances to a list to loop over
        self._instances.append(self)

    def update_vel(self):
        # Calculates acceleration in x- and y-axis for body 1.
        acceleration_x = self.force_x / self.mass
        acceleration_y = self.force_y / self.mass
        self.vel.x -= (acceleration_x * self.DT) / self.SCALE
        self.vel.y -= (acceleration_y * self.DT) / self.SCALE

        self.pos.x += self.vel.x * self.DT
        self.pos.y += self.vel.y * self.DT
        self.orbit.append((self.pos.x, self.pos.y))

    def update(self, camera_group, animation_group):
        self.animation_group = animation_group
        self.camera_group = camera_group
        # Calculate forces between all pairs of bodies
        for body1 in self._instances:
            # Reset the total forces acting on each body to zero
            body1.force_x = 0
            body1.force_y = 0
            for body2 in self._instances:
                # Ensure we're not calculating the force of a body on itself
                if body1 is not body2:
                    fx, fy = body1.move(body2)
                    body1.force_x += fx
                    body1.force_y += fy

        self.update_vel()
        self.draw()

    def move(self, body):
        # Calculates difference in x- and y-axis between the bodies
        distance_x = self.pos.x - body.pos.x
        distance_y = self.pos.y - body.pos.y
        # Calculates the distance between the bodies
        radius = (distance_y**2 + distance_x**2) ** 0.5
        # Calculates the angle between the bodies with atan2
        force = 4 / 3 * math.pi * radius
        force_x = distance_x / radius * force
        force_y = distance_y / radius * force

        # Checks if collision
        if radius < self.radius or (
            self.pos.x > self.width + 500 or self.pos.y > self.height + 500
        ):
            self.delete(body)
        else:
            # Gravitational formula.
            force = (self.G * self.mass * body.mass) / (radius / self.SCALE) ** 2
            force_x = distance_x / radius * force
            force_y = distance_y / radius * force
        return force_x, force_y

    def delete(self, body):
        if body.protected is False:
            explosion = Explosion("assets/explosion.png")
            self.animation_group.add(explosion)
            explosion.animate(body.pos)
            body.kill()
            self._instances.remove(body)

    def draw(self):
        self.zoom = self.radius * self.camera_group.scale_size

        x = self.pos.x * self.SCALE + self.width / 2
        y = self.pos.y * self.SCALE + self.height / 2

        # Orbit lines
        if len(self.orbit) > 2:
            updated_points = []

            # Shorter orbit for satellites
            if self.protected:
                max_points = 480
            else:
                max_points = 200

            for point in self.orbit:
                x, y = point
                updated_points.append(
                    (x + self.camera_group.offset.x, y + self.camera_group.offset.y)
                )

            if len(updated_points) > max_points:
                updated_points = updated_points[-max_points:]

            pygame.draw.lines(self.surface, self.color, False, updated_points, 1)

        # Camera movement Calculation
        pos = (
            self.pos.x + self.camera_group.offset.x,
            self.pos.y + self.camera_group.offset.y,
        )
        pygame.draw.circle(
            surface=self.surface,
            color=self.color,
            center=pos,
            radius=self.zoom,
        )
