""" config.py """

SCREEN_RES = [1280, 720]

TITLE = "MAYHEM by Robin Kristiansen (c) 2021"

FPS = 60


SPACESHIP_SHAPE = [(15, 0), (0, 50), (15, 40), (30, 50), (15, 0)]
# SPACESHIP_COLOR = (255, 94, 0)      # orange
# PLAYER1_COLOR = (237,114,86)
COLOR_RED =   (255, 0, 0)
COLOR_GREEN = (0, 255, 0)
COLOR_BLUE =  (0, 0, 255)
COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)

PLAYER1_COLOR = COLOR_RED
PLAYER2_COLOR = COLOR_BLUE

SPACESHIP_WIDTH = 30
SPACESHIP_HEIGHT = 50
        
BULLETSPEED = 1000
RATE_OF_FIRE = 600 # Rounds per minute
FIRE_DELAY = 1 / (RATE_OF_FIRE / 60) * 1000
