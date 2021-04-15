import pygame
import copy
from moving_object import MovingObject
from config import *


class Bullet(MovingObject):
    bullet_img = pygame.Surface([5, 5], pygame.SRCALPHA)
    pygame.draw.rect(bullet_img, ARYAN, (0, 0, 5, 5))

    def __init__(self, game, startpos, angle):
        super().__init__()
        self.image = Bullet.bullet_img
        self.rect = self.image.get_rect()
        self.game = game
        self.pos = copy.copy(startpos)
        self.angle = copy.copy(angle)
        self.vel = self.up_vector.rotate(-angle) * BULLETSPEED

    def update(self):
        self.pos += self.vel * self.game.delta_time
        self.rect = self.image.get_rect(center=self.pos)
        self.image = pygame.transform.rotate(self.bullet_img, self.rotation)
