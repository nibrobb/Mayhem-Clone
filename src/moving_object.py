""" moving_object.py """

import pygame
from pygame import Vector2


class MovingObject (pygame.sprite.Sprite):
    """
    Parent class of moving objects
    """
    def __init__(self) -> None:
        super().__init__()
        self.pos = Vector2(0,0)
        self.vel = Vector2(0,0)
        self.up_vector = Vector2(0, -1)
        self.rotation = 0
        self.moving = 0
