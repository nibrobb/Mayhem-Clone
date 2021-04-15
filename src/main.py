#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" Mayhem clone by Robin Kristiansen (c) 2021 """

import pygame
from config import *

class Game:
    """ This is a game """
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(SCREEN_RES)
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.delta_time = 0

    def run(self):
        running = True
        while running:
            self.delta_time = self.clock.tick(FPS) / 1000.0
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()

    def update(self):
        pass

    def draw(self):
        self.screen.fill((255, 0, 0))
        
        pygame.display.flip()

    def quit(self):
        pygame.quit()

if __name__ == '__main__':
    game = Game()
    while True:
        game.run()
