""" spaceship.py """
import pygame
from pygame import Vector2
from pygame import time
from moving_object import MovingObject
from bullet import Bullet
from config import *


class Spaceship(MovingObject):
    spaceship_original = pygame.Surface([SPACESHIP_WIDTH, SPACESHIP_HEIGHT], pygame.SRCALPHA)
    pygame.draw.polygon(spaceship_original, SPACESHIP_COLOR, SPACESHIP_SHAPE, 0)
    spaceship_img = pygame.transform.rotozoom(spaceship_original, 0, 0.6)
    
    def __init__(self, game, startpos):
        super().__init__()
        self.image = Spaceship.spaceship_img
        self.rect = self.image.get_rect()
        self.game = game
        self.pos = startpos

        self.last_shot = 0

    def thrust(self):
        self.vel += 2*self.up_vector.rotate(-self.rotation)

    def update(self):
        self.pos += self.vel * self.game.delta_time * self.moving
        self.rect = self.image.get_rect(center=self.pos)
        self.image = pygame.transform.rotate(self.spaceship_img, self.rotation)

    def rotate(self, angle : int):
        self.rotation += angle

    def shoot(self):
        if time.get_ticks() - self.last_shot > FIRE_DELAY:
            bullet = Bullet(self.game, self)
            self.game.all_sprites.add(bullet)
            self.last_shot = time.get_ticks()

        # bullet = Bullet(self.game, self.pos, self.rotation)
