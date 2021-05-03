""" config.py - All global configurations and constants stored here """
from pygame import Vector2

SCREEN_RES = [1280, 720]

TITLE = "MAYHEM by Robin Kristiansen (c) 2021"

FPS = 60

GRAVITY = Vector2(0, 0.1337)

SPACESHIP_SHAPE = [(15, 0), (0, 50), (15, 40), (30, 50), (15, 0)]
COLOR_RED =   (255, 0, 0)
COLOR_GREEN = (0, 255, 0)
COLOR_BLUE =  (0, 0, 255)
COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)
COLOR_GRAY = (127, 127, 127)

PLAYER1_COLOR = COLOR_RED
PLAYER2_COLOR = COLOR_BLUE

SPACESHIP_WIDTH = 30
SPACESHIP_HEIGHT = 50

SPACESHIP_MAX_SPEED = 200
SPACESHIP_MAX_SPEED_SQUARED = SPACESHIP_MAX_SPEED**2

DRAG_COEFICIENT = 0.995

BULLETSPEED = 1000
RATE_OF_FIRE = 600 # Rounds per minute
FIRE_DELAY = 1 / (RATE_OF_FIRE / 60) * 1000


BULLET_DAMAGE = 10
HIT_SCORE = 5

# Constants for placing score/info-boxes
BOTTOM_LEFT = 0
BOTTOM_RIGHT = 1
