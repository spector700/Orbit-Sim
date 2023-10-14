import sprites
import camera
import pygame
from pygame.math import Vector2 as vec2
import pytest


WIDTH = 800
HEIGHT = 800


# Define a fixture for setting up the game environment
@pytest.fixture
def game_environment():
    pygame.init()
    pygame.display.set_mode([WIDTH, HEIGHT])
    group = camera.CameraGroup()

    earth = sprites.Bodies(
        group,
        pos=vec2(WIDTH / 2, HEIGHT / 2),
        radius=100,
        color="#6b93d6",
        mass=5.97219e24,
        vel=vec2(-24.947719394204714 / 2, 0),
        protected=True,
    )
    moon = sprites.Bodies(
        group,
        pos=vec2(WIDTH, HEIGHT / 3),
        radius=20,
        color="gray",
        mass=7.349e22,
        vel=vec2(1023, 0),
        protected=True,
    )

    yield group, earth, moon  # Provide the game environment to the tests

    # Clean up after the tests (e.g., closing the game window)
    pygame.quit()
    sprites.Bodies._instances.clear()


def test_move(game_environment):
    _, earth, moon = game_environment

    force_x, force_y = moon.move(earth)

    assert abs(force_y) > 2e19
    assert abs(force_x) > 7e19


def test_update_vel(game_environment):
    _, _, moon = game_environment

    moon.update_vel()
    assert moon.pos.x > 800
    assert moon.pos.y < 400


def test_sat(game_environment):
    group, _, _ = game_environment

    sprites.Bodies(
        group,
        pos=vec2(420, 420),
        radius=9,
        mass=2000,
        vel=vec2(1370, 100),
    )

    assert len(sprites.Bodies._instances) == 3


def test_delete(game_environment):
    group, _, _ = game_environment

    sat = sprites.Bodies(
        group,
        pos=vec2(420, 420),
        radius=9,
        mass=2000,
        vel=vec2(1370, 100),
    )

    sat.delete(sat)
    assert sat.alive


if __name__ == "__main__":
    pytest.main()
