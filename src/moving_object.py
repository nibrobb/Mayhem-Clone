import pygame
from pygame import Vector2


class MovingObject (pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = None       # Bare deklarasjon for å vise at de finnes
        self.rect = None
        self.pos = Vector2(0,0)
        self.vel = Vector2(0,0)
        self.up_vector = Vector2(0, -1)
        self.rotation = 0
        self.gravity = 9.8
        self.moving = 0