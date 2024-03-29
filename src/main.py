#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" main.py - Mayhem clone by Robin Kristiansen (c) 2021 """

import pygame
from pygame.constants import BLEND_ADD
from config import *
from floor_wall import FloorWall
from refuel_station import RefuelStation
from spaceship import Spaceship
from obstacle import Obstacle
from bullet import Bullet

class Game:
    """ Mayhem-clone made by Robin Kristiansen """
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode(SCREEN_RES)
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.delta_time = 0
        self.ships = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()

        self.run()


    def run(self) -> None:
        """ Main game-loop, runs until player quits """
        running = True

        self.spawn_spaceships()
        self.spawn_floor_wall()
        self.spawn_obstacles()
        self.spawn_refuel_station()

        while running:
            self.delta_time = self.clock.tick(FPS) / 1000.0
            self.events()
            self.update()
            self.collision()
            self.draw()


    def spawn_spaceships(self) -> None:
        """ Spawns players spaceships """
        self.player1 = Spaceship(self, (SCREEN_RES[0]//3, SCREEN_RES[1] - 50), COLOR_RED)
        self.player2 = Spaceship(self, (2*SCREEN_RES[0]//3, SCREEN_RES[1] - 50), COLOR_BLUE)
        self.ships.add(self.player1, self.player2)
        self.all_sprites.add(self.player1, self.player2)


    def spawn_floor_wall(self) -> None:
        """ Spawn in walls, floors and ceiling """
        self.floor = FloorWall(SCREEN_RES[0], 20, (SCREEN_RES[0], SCREEN_RES[1]), COLOR_DARK_GRAY)
        self.roof  = FloorWall(SCREEN_RES[0], 20, (SCREEN_RES[0], 20), COLOR_DARK_GRAY)
        self.wall1 = FloorWall(20, SCREEN_RES[1], (20, SCREEN_RES[1]), COLOR_DARK_GRAY)
        self.wall2 = FloorWall(20, SCREEN_RES[1], (SCREEN_RES[0], SCREEN_RES[1]), COLOR_DARK_GRAY)
        self.all_sprites.add(self.floor, self.roof, self.wall1, self.wall2)


    def spawn_obstacles(self) -> None:
        """ Spawns obstacle(s) """
        obs = Obstacle(COLOR_GREEN, 100, 100, (SCREEN_RES[0]//2, SCREEN_RES[1]//2))
        self.all_sprites.add(obs)

    def spawn_refuel_station(self) -> None:
        """ Spawns refueling stations for the two players or \"teams\" """
        self.blue_station = RefuelStation(TEAM_BLUE, (100, 500))
        self.red_station = RefuelStation(TEAM_RED, (SCREEN_RES[0] - 100, 500))
        self.all_sprites.add(self.blue_station, self.red_station)

    def collision(self) -> None:
        """ Handles collision (not very optimzed) """

        collide_bullet_floor_wall = pygame.sprite.groupcollide(Bullet.group, FloorWall.group, False, False)
        for bullet in collide_bullet_floor_wall:
            bullet.kill()

        collide_bullet_obstacle = pygame.sprite.groupcollide(Bullet.group, Obstacle.group, False, False)
        for bullet in collide_bullet_obstacle:
            bullet.kill()


        if self.player1.alive():
            collide_player1_bullet = pygame.sprite.spritecollide(self.player1, self.player2.bullets, False)
            for c in collide_player1_bullet:
                c.kill()
                self.player1.health -= BULLET_DAMAGE
                self.player2.score += HIT_SCORE

            collide_player1_floor_wall = pygame.sprite.spritecollide(self.player1, FloorWall.group, False)
            for c in collide_player1_floor_wall:
                self.player1.vel *= -1
                self.player1.health -= WALL_COLLISION_DAMAGE
            
            collide_player1_obstacle = pygame.sprite.spritecollide(self.player1, Obstacle.group, False)
            for c in collide_player1_obstacle:
                self.player1.vel *= -1
                self.player1.health -= OBSTACLE_HIT_DAMAGE

            if pygame.Rect.colliderect(self.player1.rect, self.red_station.rect) == True:
                self.player1.vel *= -0.99
                if self.player1.fuel < FUEL_TANK_SIZE:
                    self.player1.fuel += 1

        if self.player2.alive():
            collide_player2_bullet = pygame.sprite.spritecollide(self.player2, self.player1.bullets, False)
            for c in collide_player2_bullet:
                c.kill()
                self.player2.health -= BULLET_DAMAGE
                self.player1.score += HIT_SCORE

            collide_player2_floor_wall = pygame.sprite.spritecollide(self.player2, FloorWall.group, False)
            for c in collide_player2_floor_wall:
                self.player2.vel *= -1
                self.player2.health -= WALL_COLLISION_DAMAGE

            collide_player2_obstacle = pygame.sprite.spritecollide(self.player2, Obstacle.group, False)
            for c in collide_player2_obstacle:
                self.player2.vel *= -1
                self.player2.health -= OBSTACLE_HIT_DAMAGE

            if pygame.Rect.colliderect(self.player2.rect, self.blue_station.rect) == True:
                self.player2.vel *= -0.99
                if self.player2.fuel < FUEL_TANK_SIZE:
                    self.player2.fuel += 1




    def events(self) -> None:
        """ Handles input """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()
            if event.type == pygame.KEYDOWN:
                self.player1.moving = 1
                self.player2.moving = 1
                if event.key == pygame.K_r:
                    self.reset()
                    

        keys = pygame.key.get_pressed()

        #---------- Player 1 ----------#
        if self.player1.alive():
            if keys[ord('w')]:
                self.player1.thrust()       # Thrust
            if keys[ord('a')]:
                self.player1.rotate(5)      # Rotate left (ccw)
            if keys[ord('d')]:
                self.player1.rotate(-5)     # Roatate right (cw)
            if keys[pygame.K_SPACE]:
                self.player1.fire()         # Fire

        #---------- Player 2 ----------#
        if self.player2.alive():
            if keys[pygame.K_LEFT]:
                self.player2.rotate(5)      # Rotate left (ccw)
            if keys[pygame.K_RIGHT]:
                self.player2.rotate(-5)     # Rotate right (cw)
            if keys[pygame.K_UP]:
                self.player2.thrust()       # Thrust
            if keys[pygame.K_RCTRL]:
                self.player2.fire()         # Fire


    def update(self) -> None:
        """ Calls update() on sprite groups, only used for MovingObjects """
        self.ships.update()
        self.all_sprites.update()
    
    def display_info(self) -> None:
        """ Used to display info about players, such as score, health, ammo and fuel """
        text_size = 20
        font_family = "Arial"

        player1_text_list = []

        # Player1 name
        player1_name_text = self.setup_font(str(self.player1.name), font_family, 22, COLOR_WHITE)
        player1_text_list.append(player1_name_text)
        # Player1 ammo
        player1_ammo_text = self.setup_font("Ammo: {}".format(self.player1.ammo), font_family, text_size, COLOR_WHITE)
        player1_text_list.append(player1_ammo_text)
        # Player1 health
        player1_health_text = self.setup_font("Health: {}".format(self.player1.health), font_family, text_size, COLOR_WHITE)
        player1_text_list.append(player1_health_text)
        # Player1 fuel
        player1_fuel_text = self.setup_font("Fuel: {:.0f}".format(self.player1.fuel), font_family, text_size, COLOR_WHITE)
        player1_text_list.append(player1_fuel_text)
        #Player1 score
        player1_score_text = self.setup_font("Score: {}".format(self.player1.score), font_family, text_size, COLOR_WHITE)
        player1_text_list.append(player1_score_text)

        self.blit_text(player1_text_list, BOTTOM_LEFT)



        player2_text_list = []

        # Player2 name
        player2_name_text = self.setup_font(str(self.player2.name), font_family, 22, COLOR_WHITE)
        player2_text_list.append(player2_name_text)
        # Player2 ammo
        player2_ammo_text = self.setup_font("Ammo: {}".format(self.player2.ammo), font_family, text_size, COLOR_WHITE)
        player2_text_list.append(player2_ammo_text)
        # Player2 health
        player2_health_text = self.setup_font("Health: {}".format(self.player2.health), font_family, text_size, COLOR_WHITE)
        player2_text_list.append(player2_health_text)
        # Player2 fuel
        player2_fuel_text = self.setup_font("Fuel: {:.0f}".format(self.player2.fuel), font_family, text_size, COLOR_WHITE)
        player2_text_list.append(player2_fuel_text)
        #Player2 score
        player2_score_text = self.setup_font("Score: {}".format(self.player2.score), font_family, text_size, COLOR_WHITE)
        player2_text_list.append(player2_score_text)

        self.blit_text(player2_text_list, BOTTOM_RIGHT)



    def setup_font(self, text, font, size, color) -> pygame.Surface:
        """ Returns a surface with the chosen text """
        text_font = pygame.font.SysFont(font, size)
        text_surface = text_font.render(text, True, color)
        return text_surface
    
    def blit_text(self, text_list, alignment) -> None:
        """ Prints all the text in text_list to the screen """

        offset = 0
        background_width = 150
        background_height = 120
        pos = [0, 0]

        if alignment == BOTTOM_LEFT:
            pos[0] = 0
            pos[1] = SCREEN_RES[1] - background_height
        elif alignment == BOTTOM_RIGHT:
            pos[0] = SCREEN_RES[0] - background_width
            pos[1] = SCREEN_RES[1] - background_height
        else:
            pos = (0,0)

        background = pygame.Surface((background_width, background_height))
        background.fill(COLOR_GRAY)
        self.screen.blit(background, pos)

        for text in text_list:
            self.screen.blit(text, (pos[0] + 4, pos[1] + offset))
            offset += text.get_height()

    def draw(self) -> None:
        """ Draw all visible sprites to the screen """
        self.screen.fill(COLOR_BLACK)
        for sprite in self.all_sprites:
            self.screen.blit(sprite.image, (sprite.rect.x, sprite.rect.y))
        self.display_info()
        pygame.display.flip()

    def reset(self) -> None:
        """ Reset players stats except score """
        self.player1.reset()
        self.player2.reset()
        self.all_sprites.add(self.player1, self.player2)

    def quit(self) -> None:
        """ Quit the game """
        pygame.quit()


if __name__ == '__main__':
    game = Game()
