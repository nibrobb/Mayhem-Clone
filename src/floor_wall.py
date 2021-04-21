import pygame
from moving_object import MovingObject
from config import *

class FloorWall(MovingObject):
    group = pygame.sprite.Group()
    def __init__(self, width, height, pos):
        super().__init__()
        floor_wall_img = pygame.Surface([width, height])
        # pygame.draw.rect(floor_wall_img, ARYAN, (0, 0, width, height))
        floor_wall_img.fill(ARYAN)
        self.image = floor_wall_img
        self.rect = self.image.get_rect(x=pos[0]-width, y=pos[1]-height)
        self.pos = pos
        FloorWall.group.add(self)
