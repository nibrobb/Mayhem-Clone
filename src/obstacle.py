""" obstacle.py """
import pygame
from static_object import StaticObject

class Obstacle(StaticObject):

    group = pygame.sprite.Group()

    def __init__(self, color, width, height, pos):
        super().__init__()

        self.pos = pos

        self.canvas = pygame.Surface([width, height], pygame.SRCALPHA)
        pygame.draw.rect(self.canvas, color, (0, 0, width, height))

        self.image = self.canvas
        self.rect = self.image.get_rect(center=pos)

        Obstacle.group.add(self)
