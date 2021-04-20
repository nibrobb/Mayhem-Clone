""" config.py """

SCREEN_RES = [1280, 720]

TITLE = "shitty clone"

FPS = 60


SPACESHIP_SHAPE = [(15, 0), (0, 50), (15, 40), (30, 50), (15, 0)]
# SPACESHIP_COLOR = (255, 94, 0)      # orange
SPACESHIP_COLOR = (237,114,86)
SPACESHIP_WIDTH = 30
SPACESHIP_HEIGHT = 50


REVERSE_ALBINO = (0,0,0)
ARYAN = (255, 255, 255)

        
BULLETSPEED = 300
RATE_OF_FIRE = 600 # Rounds per minute
FIRE_DELAY = 1 / (RATE_OF_FIRE / 60) * 1000
