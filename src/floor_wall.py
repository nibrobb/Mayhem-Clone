""" floor_wall.py """
from typing import Tuple
import pygame

from config import *
from static_object import StaticObject

class FloorWall(StaticObject):
    """ Create a boundry, wall or floor, depending on you disposition """
    group = pygame.sprite.Group()
    def __init__(self, width, height, pos, color : Tuple[int, int, int] = COLOR_WHITE) -> None:
        super().__init__()
        
        self.width = width
        self.height = height
        self.pos = pos
        self.color = color

        # Draw a white filled rectangle width the specified width and height
        floor_wall_img = pygame.Surface([self.width, self.height])
        floor_wall_img.fill(self.color)

        self.image = floor_wall_img
        
        self.rect = self.image.get_rect(x=pos[0]-width, y=pos[1]-height)
        FloorWall.group.add(self)
