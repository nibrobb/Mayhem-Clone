""" spaceship.py """
import pygame
from pygame import Vector2
from pygame import time
from moving_object import MovingObject
from bullet import Bullet
from config import *


class Spaceship(MovingObject):
    """ Create a new spaceship using this class """
    callcount = 0
    def __init__(self, game, startpos, color, name : str = "Player") -> None:
        """ Make a new Spaceship with fuel, ammo, a name and more """
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

        # Give a name to the players if they have not specified a unique name
        if name == "Player":
            self.name = name + str(Spaceship.callcount)
        else:
            self.name = name
        self.health = 100   # Percentage of health
        self.ammo = 30*10   # Number of bullets
        self.fuel = 500     # Liters of fuel
        self.score = 0      # Points

    def thrust(self, factor = 5) -> None:
        """ Accelerate the ship in the direction in which it is pointing """
        if self.vel.magnitude_squared() < SPACESHIP_MAX_SPEED_SQUARED:
            self.vel += factor * self.up_vector.rotate(-self.rotation)


    def update(self) -> None:
        """ Update position and apply gravity and drag, and set new image """
        self.vel += GRAVITY
        self.vel *= DRAG_COEFICIENT
        self.fuel -= 0.1337 * self.moving
        self.pos += self.vel * self.game.delta_time * self.moving
        self.rect = self.image.get_rect(center=self.pos)
        self.image = pygame.transform.rotate(self.spaceship_img, self.rotation)
        if self.health <= 0:
            self.kill()
            print("{} died".format(self.name))
        print("{}'s speed is {:.2f}".format(self.name, self.vel.magnitude()))

    def rotate(self, angle : int) -> None:
        self.rotation += angle

    def fire(self) -> None:
        if time.get_ticks() - self.last_shot > FIRE_DELAY and self.ammo > 0:
            self.ammo -= 1
            bullet = Bullet(self.game, self)
            self.bullets.add(bullet)
            self.game.all_sprites.add(bullet)
            self.last_shot = time.get_ticks()
