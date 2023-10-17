# Pygame Orbit Simulation

### Showcase
[![Video](https://img.youtube.com/vi/ML5fOiTLlwk/0.jpg)](https://www.youtube.com/watch?v=ML5fOiTLlwk)

## About
This is a Python pygame simulation of celestial bodies orbiting in space, created using the Pygame library. 
It allows you to visualize the movement of planets, stars, and other celestial objects in a simple and interactive way.
Accurate mass and velocity are used for the calculations for the orbit.



## Files

- __project.py__: Initializes all the necessary classes, background music, sprite groups, and the main game loop.

- __camera.py__: Contains the class responsible for camera panning and the calculation of camera offsets, which other classes use to obtain updated positions.

- __sprites.py__: Includes the class for background stars, specifying their quantity, color, random positions, and sizes. This file also contains the "Bodies" class, which calculates the force of gravity, velocity, and interactions with other celestial bodies for Earth, the Moon, and satellites.

- __spritesheet.py__: Features the class for extracting individual images from a spritesheet, adding them to a list, displaying images, and playing collision sounds. This class is called by the "Bodies" class and removes satellite instances upon collision.

- __test_project.py__: This file is designed for testing the classes in a controlled game environment.



## Controls
| Control               | Action                                       |
|-----------------------|----------------------------------------------|
| Left Mouse Button     | Pan camera                                   |
| Mouse Wheel           | Zoom in/out                                  |
| Right Mouse Button    | Spawn Satellite                    |
| F          | Show FPS                     |


