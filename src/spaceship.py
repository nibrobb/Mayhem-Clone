""" spaceship.py """
import pygame
from pygame import Vector2
from pygame import time
from moving_object import MovingObject
from bullet import Bullet
from config import *


class Spaceship(MovingObject):
    callcount = 0
    def __init__(self, game, startpos, color, name : str = "Player"):
        super().__init__()
        Spaceship.callcount += 1

        self.spaceship_original = pygame.Surface([SPACESHIP_WIDTH, SPACESHIP_HEIGHT], pygame.SRCALPHA)
        pygame.draw.polygon(self.spaceship_original, color, SPACESHIP_SHAPE, 0)
        self.spaceship_img = pygame.transform.rotozoom(self.spaceship_original, 0, 0.6)

        self.image = self.spaceship_img
        self.rect = self.image.get_rect()
        self.game = game
        self.pos = startpos

        self.last_shot = 0

        self.bullets = pygame.sprite.Group()

        self.name = name + str(Spaceship.callcount)
        self.health = 100
        self.ammo = 30*10
        self.score = 0

    def thrust(self, factor):
        self.vel += factor * self.up_vector.rotate(-self.rotation)
    
    def dethrust(self):
        self.vel *= 0.95

    def update(self):
        self.pos += self.vel * self.game.delta_time * self.moving
        self.rect = self.image.get_rect(center=self.pos)
        self.image = pygame.transform.rotate(self.spaceship_img, self.rotation)
        if self.health <= 0:
            print("{} died".format(self.name))
            self.kill()

    def rotate(self, angle : int):
        self.rotation += angle

    def fire(self):
        if time.get_ticks() - self.last_shot > FIRE_DELAY and self.ammo > 0:
            self.ammo -= 1
            bullet = Bullet(self.game, self)
            self.bullets.add(bullet)
            self.game.all_sprites.add(bullet)
            self.last_shot = time.get_ticks()

        # bullet = Bullet(self.game, self.pos, self.rotation)
