import pygame
import pytest
from pygame.math import Vector2 as vec2

import camera
import sprites

WIDTH = 1920
HEIGHT = 1080


# Define a fixture for setting up the game environment
@pytest.fixture
def game_environment():
    pygame.init()
    pygame.display.set_mode([WIDTH, HEIGHT])
    camera_group = camera.CameraGroup()
    animation_group = pygame.sprite.Group()
    bodies_group = pygame.sprite.Group()

    bodies_group.update(camera_group, animation_group)

    earth = sprites.Bodies(
        bodies_group,
        pos=vec2(WIDTH / 2, HEIGHT / 2),
        radius=100,
        color="#6b93d6",
        mass=5.97219e24,
        vel=vec2(-24.947719394204714 / 2, 0),
        protected=True,
    )
    moon = sprites.Bodies(
        bodies_group,
        pos=vec2(WIDTH / 2, HEIGHT / 2 + 270),
        radius=20,
        color="gray",
        mass=7.349e22,
        vel=vec2(1023, 0),
        protected=True,
    )

    # Provide the game environment to the tests
    yield bodies_group, earth, moon

    # Clean up after the tests (e.g., closing the game window)
    pygame.quit()
    sprites.Bodies._instances.clear()


def test_move(game_environment):
    _, earth, moon = game_environment

    force_x, force_y = moon.move(earth)

    assert abs(force_y) > 2e19
    assert abs(force_x) == 0.0


def test_update_vel(game_environment):
    _, _, moon = game_environment

    moon.update_vel()
    assert moon.pos.x > WIDTH / 2
    assert moon.pos.y > HEIGHT / 2


def test_sat(game_environment):
    bodies_group, _, _ = game_environment

    sprites.Bodies(
        bodies_group,
        pos=vec2(420, 420),
        radius=9,
        mass=2000,
        vel=vec2(1370, 100),
    )

    assert len(sprites.Bodies._instances) == 3


if __name__ == "__main__":
    pytest.main()
