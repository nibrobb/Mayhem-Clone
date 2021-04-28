""" floor_wall.py """
import pygame

from config import *
from static_object import StaticObject

class FloorWall(StaticObject):
    """ Create a boundry, wall or floor, depending on you disposition """
    group = pygame.sprite.Group()
    def __init__(self, width, height, pos):
        super().__init__()
        floor_wall_img = pygame.Surface([width, height])
        # pygame.draw.rect(floor_wall_img, ARYAN, (0, 0, width, height))
        floor_wall_img.fill(COLOR_WHITE)
        self.image = floor_wall_img
        self.rect = self.image.get_rect(x=pos[0]-width, y=pos[1]-height)
        self.pos = pos
        FloorWall.group.add(self)
