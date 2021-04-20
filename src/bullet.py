import pygame
import copy
from moving_object import MovingObject
from config import *


class Bullet(MovingObject):
    """ Creates a single bullet that will fly in the same direction as the caller """
    bullet_img = pygame.Surface([5, 5], pygame.SRCALPHA)
    pygame.draw.rect(bullet_img, ARYAN, (0, 0, 5, 5))

    def __init__(self, game, spaceship):
        # game:         The game object
        # spaceship:    The ship that called the shot
        super().__init__()
        self.image = Bullet.bullet_img
        self.rect = self.image.get_rect()
        self.game = game
        self.pos = copy.copy(spaceship.pos)          # using shallow-copy to only copy value
        self.angle = copy.copy(spaceship.rotation)   # -||-
        self.vel = self.up_vector.rotate(-self.angle) * BULLETSPEED

    def update(self):
        self.pos += self.vel * self.game.delta_time
        self.rect = self.image.get_rect(center=self.pos)
        self.image = pygame.transform.rotate(self.bullet_img, self.rotation)
