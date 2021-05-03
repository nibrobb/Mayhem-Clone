""" static_object.py """

import pygame

class StaticObject(pygame.sprite.Sprite):
    """
    Parent class of non-moving, static structures
    such as walls, floors or any other immovable object
    """
    def __init__(self) -> None:
        super().__init__()
        self.pos = (0, 0)
