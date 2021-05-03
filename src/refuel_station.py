""" refuel_station.py """

import pygame
from static_object import StaticObject
from config import *


class RefuelStation(StaticObject):
    def __init__(self, team, pos) -> None:
        super().__init__()
        if team == TEAM_RED:
            self.color = COLOR_RED
        elif team == TEAM_BLUE:
            self.color = COLOR_BLUE
        else:
            raise ValueError

        self.width = 50
        self.height = 20
        
        self.pos = pos

        self.og_img = pygame.Surface([self.width, self.height])
        pygame.draw.rect(self.og_img, self.color, (0, 0, self.width, self.height))

        self.image = self.og_img
        self.rect = self.image.get_rect(center=self.pos)