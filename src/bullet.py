""" bullet.py - Defines bullets """
import copy
import pygame
from moving_object import MovingObject
from config import *


class Bullet(MovingObject):
    """ Creates a single bullet that will fly in the same direction as the caller """
    bullet_img = pygame.Surface([5, 5], pygame.SRCALPHA)
    pygame.draw.rect(bullet_img, COLOR_WHITE, (0, 0, 5, 5))

    group = pygame.sprite.Group()

    def __init__(self, game, spaceship) -> None:
        super().__init__()
        self.shooter = spaceship

        self.image = Bullet.bullet_img
        self.rect = self.image.get_rect()
        self.game = game
        self.pos = copy.copy(spaceship.pos)          # using shallow-copy to only copy value
        self.angle = copy.copy(spaceship.rotation)   # -||-
        self.vel = self.up_vector.rotate(-self.angle) * BULLETSPEED
        Bullet.group.add(self)

    def update(self) -> None:
        """ Make the bullet move and correctly set the image """
        self.pos += self.vel * self.game.delta_time
        self.rect = self.image.get_rect(center=self.pos)
        self.image = pygame.transform.rotate(self.bullet_img, self.rotation)
