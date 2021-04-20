#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" Mayhem clone by Robin Kristiansen (c) 2021 """

import pygame
from config import *
from floor_wall import FloorWall
from spaceship import Spaceship

class Game:
    """ This is a game """
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(SCREEN_RES)
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.delta_time = 0
        # self.load_spaceship()
        self.ships = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()


    # def load_spaceship(self):
    #     spaceship_original = pygame.Surface([SPACESHIP_WIDTH, SPACESHIP_HEIGHT], pygame.SRCALPHA)
    #     pygame.draw.polygon(spaceship_original, SPACESHIP_COLOR, 0)
    #     self.spaceship_img = pygame.transform.rotozoom(spaceship_original, 0, 0.6)

    def run(self):
        running = True

        self.spawn_spaceship()
        self.floor = FloorWall(SCREEN_RES[0], 20, (SCREEN_RES[0], SCREEN_RES[1]))
        
        self.all_sprites.add(self.floor)

        while running:
            self.delta_time = self.clock.tick(FPS) / 1000.0
            self.events()
            self.update()
            self.draw()

    def spawn_spaceship(self):
        self.player1 = Spaceship(self, (420, 69))
        # self.player2 = Spaceship(self)
        self.player1.moving = 1
        # self.player2.moving = 1
        self.ships.add(self.player1)
        self.all_sprites.add(self.player1)
        # self.ships.add(self.player2)

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()
            # if event.type == pygame.KEYDOWN:
            #     if event.key == pygame.K_SPACE:
            #         self.player1.shoot()        # Shoot

        keys = pygame.key.get_pressed()
        if keys[ord('w')]:      # Thrust
            self.player1.thrust()
        if keys[ord('a')]:      # Rotate left (ccw)
            self.player1.rotate(5)
        # if keys[ord('s')]:      # Thrust
        #      self.player1.thrust()
        if keys[ord('d')]:      # Rotate right (cc)
            self.player1.rotate(-5)
        if keys[pygame.K_SPACE]:
            self.player1.shoot()
            

    def update(self):
        self.ships.update()
        self.all_sprites.update()

    def draw(self):
        self.screen.fill(REVERSE_ALBINO)
        for sprite in self.all_sprites:
            self.screen.blit(sprite.image, (sprite.rect.x, sprite.rect.y))
        pygame.display.flip()

    def quit(self):
        pygame.quit()

if __name__ == '__main__':
    game = Game()
    while True:
        game.run()
