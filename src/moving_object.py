""" moving_object.py """
import pygame
from pygame import Vector2


class MovingObject (pygame.sprite.Sprite):
    """ Parent class of moving objects
        Must not be instantiated
    """
    def __init__(self):
        super().__init__()
        self.pos = Vector2(0,0)
        self.vel = Vector2(0,0)
        self.up_vector = Vector2(0, -1)
        self.rotation = 0
        
        self.gravity = 9.8
        self.moving = 0