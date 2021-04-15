import pygame
from moving_object import MovingObject
from config import *


class Bullet(MovingObject):
    bullet_img = pygame.Surface([10, 10], pygame.SRCALPHA)
    pygame.draw.rect(bullet_img, ARYAN, (0, 0, 10, 10))

    def __init__(self, game, direction):
        super().__init__()
        self.vel = direction * 10
        self.game = game

    def update(self):
        self.pos += self.vel * self.game.delta_time
        self.rect = self.image.get_rect(center=self.pos)
        self.image = pygame.transform.rotate(self.bullet_img, self.rotation)
